import os
import glob
import json
import pkg_resources
import numpy as np
from scipy.io.wavfile import read
import torch

f0_bin = 256
f0_max = 1100.0
f0_min = 50.0
f0_mel_min = 1127 * np.log(1 + f0_min / 700)
f0_mel_max = 1127 * np.log(1 + f0_max / 700)

def normalize_f0(f0, x_mask, uv, random_scale=True):
    # calculate means based on x_mask
    uv_sum = torch.sum(uv, dim=1, keepdim=True)
    uv_sum[uv_sum == 0] = 9999
    means = torch.sum(f0[:, 0, :] * uv, dim=1, keepdim=True) / uv_sum

    if random_scale:
        factor = torch.Tensor(f0.shape[0], 1).uniform_(0.8, 1.2).to(f0.device)
    else:
        factor = torch.ones(f0.shape[0], 1).to(f0.device)
    # normalize f0 based on means and factor
    f0_norm = (f0 - means.unsqueeze(-1)) * factor.unsqueeze(-1)
    if torch.isnan(f0_norm).any():
        exit(0)
    return f0_norm * x_mask


def interpolate_f0(f0):
    '''
    对F0进行插值处理
    '''

    data = np.reshape(f0, (f0.size, 1))

    vuv_vector = np.zeros((data.size, 1), dtype=np.float32)
    vuv_vector[data > 0.0] = 1.0
    vuv_vector[data <= 0.0] = 0.0

    ip_data = data

    frame_number = data.size
    last_value = 0.0
    for i in range(frame_number):
        if data[i] <= 0.0:
            j = i + 1
            for j in range(i + 1, frame_number):
                if data[j] > 0.0:
                    break
            if j < frame_number - 1:
                if last_value > 0.0:
                    step = (data[j] - data[i - 1]) / float(j - i)
                    for k in range(i, j):
                        ip_data[k] = data[i - 1] + step * (k - i + 1)
                else:
                    for k in range(i, j):
                        ip_data[k] = data[j]
            else:
                for k in range(i, frame_number):
                    ip_data[k] = last_value
        else:
            ip_data[i] = data[i]
            last_value = data[i]

    return ip_data[:,0], vuv_vector[:,0]


def compute_f0_parselmouth(wav_numpy, p_len=None, sampling_rate=44100, hop_length=512):
    import parselmouth
    x = wav_numpy
    if p_len is None:
        p_len = x.shape[0]//hop_length
    else:
        assert abs(p_len-x.shape[0]//hop_length) < 4, "pad length error"
    time_step = hop_length / sampling_rate * 1000
    f0_min = 50
    f0_max = 1100
    f0 = parselmouth.Sound(x, sampling_rate).to_pitch_ac(
        time_step=time_step / 1000, voicing_threshold=0.6,
        pitch_floor=f0_min, pitch_ceiling=f0_max).selected_array['frequency']

    pad_size=(p_len - len(f0) + 1) // 2
    if(pad_size>0 or p_len - len(f0) - pad_size>0):
        f0 = np.pad(f0,[[pad_size,p_len - len(f0) - pad_size]], mode='constant')
    return f0

def resize_f0(x, target_len):
    source = np.array(x)
    source[source<0.001] = np.nan
    target = np.interp(np.arange(0, len(source)*target_len, len(source))/ target_len, np.arange(0, len(source)), source)
    res = np.nan_to_num(target)
    return res

def compute_f0_dio(wav_numpy, p_len=None, sampling_rate=44100, hop_length=512):
    import pyworld
    if p_len is None:
        p_len = wav_numpy.shape[0]//hop_length
    f0, t = pyworld.dio(
        wav_numpy.astype(np.double),
        fs=sampling_rate,
        f0_ceil=800,
        frame_period=1000 * hop_length / sampling_rate,
    )
    f0 = pyworld.stonemask(wav_numpy.astype(np.double), f0, t, sampling_rate)
    for index, pitch in enumerate(f0):
        f0[index] = round(pitch, 1)
    return resize_f0(f0, p_len)

def f0_to_coarse(f0):
  is_torch = isinstance(f0, torch.Tensor)
  f0_mel = 1127 * (1 + f0 / 700).log() if is_torch else 1127 * np.log(1 + f0 / 700)
  f0_mel[f0_mel > 0] = (f0_mel[f0_mel > 0] - f0_mel_min) * (f0_bin - 2) / (f0_mel_max - f0_mel_min) + 1

  f0_mel[f0_mel <= 1] = 1
  f0_mel[f0_mel > f0_bin - 1] = f0_bin - 1
  f0_coarse = (f0_mel + 0.5).long() if is_torch else np.rint(f0_mel).astype(np.int)
  assert f0_coarse.max() <= 255 and f0_coarse.min() >= 1, (f0_coarse.max(), f0_coarse.min())
  return f0_coarse


def get_hubert_model():
  vec_path = pkg_resources.resource_filename(__name__, "hubert/checkpoint_best_legacy_500.pt")
  print("load model(s) from {}".format(vec_path))
  from fairseq import checkpoint_utils
  models, saved_cfg, task = checkpoint_utils.load_model_ensemble_and_task(
    [vec_path],
    suffix="",
  )
  model = models[0]
  model.eval()
  return model

def get_hubert_content(hmodel, wav_16k_tensor):
  feats = wav_16k_tensor
  if feats.dim() == 2:  # double channels
    feats = feats.mean(-1)
  assert feats.dim() == 1, feats.dim()
  feats = feats.view(1, -1)
  padding_mask = torch.BoolTensor(feats.shape).fill_(False)
  inputs = {
    "source": feats.to(wav_16k_tensor.device),
    "padding_mask": padding_mask.to(wav_16k_tensor.device),
    "output_layer": 9,  # layer 9
  }
  with torch.no_grad():
    logits = hmodel.extract_features(**inputs)
    feats = hmodel.final_proj(logits[0])
  return feats.transpose(1, 2)


def get_content(cmodel, y):
    with torch.no_grad():
        c = cmodel.extract_features(y.squeeze(1))[0]
    c = c.transpose(1, 2)
    return c


def load_checkpoint(checkpoint_path, model, optimizer=None, skip_optimizer=False):
    assert os.path.isfile(checkpoint_path)
    checkpoint_dict = torch.load(checkpoint_path, map_location='cpu')
    iteration = checkpoint_dict['iteration']
    learning_rate = checkpoint_dict['learning_rate']
    if optimizer is not None and not skip_optimizer and checkpoint_dict['optimizer'] is not None:
        optimizer.load_state_dict(checkpoint_dict['optimizer'])
    saved_state_dict = checkpoint_dict['model']
    if hasattr(model, 'module'):
        state_dict = model.module.state_dict()
    else:
        state_dict = model.state_dict()
    new_state_dict = {}
    for k, v in state_dict.items():
        try:
            # assert "dec" in k or "disc" in k
            # print("load", k)
            new_state_dict[k] = saved_state_dict[k]
            assert saved_state_dict[k].shape == v.shape, (saved_state_dict[k].shape, v.shape)
        except:
            print("error, %s is not in the checkpoint" % k)
            new_state_dict[k] = v
    if hasattr(model, 'module'):
        model.module.load_state_dict(new_state_dict)
    else:
        model.load_state_dict(new_state_dict)
    return model, optimizer, learning_rate, iteration


def summarize(writer, global_step, scalars={}, histograms={}, images={}, audios={}, audio_sampling_rate=22050):
  for k, v in scalars.items():
    writer.add_scalar(k, v, global_step)
  for k, v in histograms.items():
    writer.add_histogram(k, v, global_step)
  for k, v in images.items():
    writer.add_image(k, v, global_step, dataformats='HWC')
  for k, v in audios.items():
    writer.add_audio(k, v, global_step, audio_sampling_rate)


def latest_checkpoint_path(dir_path, regex="G_*.pth"):
  f_list = glob.glob(os.path.join(dir_path, regex))
  f_list.sort(key=lambda f: int("".join(filter(str.isdigit, f))))
  x = f_list[-1]
  print(x)
  return x

def load_wav_to_torch(full_path):
  sampling_rate, data = read(full_path)
  return torch.FloatTensor(data.astype(np.float32)), sampling_rate


def load_filepaths_and_text(filename, split="|"):
  with open(filename, encoding='utf-8') as f:
    filepaths_and_text = [line.strip().split(split) for line in f]
  return filepaths_and_text

def get_hparams_from_file(config_path):
  with open(config_path, "r") as f:
    data = f.read()
  config = json.loads(data)

  hparams =HParams(**config)
  return hparams


def repeat_expand_2d(content, target_len):
    # content : [h, t]

    src_len = content.shape[-1]
    target = torch.zeros([content.shape[0], target_len], dtype=torch.float).to(content.device)
    temp = torch.arange(src_len+1) * target_len / src_len
    current_pos = 0
    for i in range(target_len):
        if i < temp[current_pos+1]:
            target[:, i] = content[:, current_pos]
        else:
            current_pos += 1
            target[:, i] = content[:, current_pos]

    return target


class HParams():
  def __init__(self, **kwargs):
    for k, v in kwargs.items():
      if type(v) == dict:
        v = HParams(**v)
      self[k] = v

  def keys(self):
    return self.__dict__.keys()

  def items(self):
    return self.__dict__.items()

  def values(self):
    return self.__dict__.values()

  def __len__(self):
    return len(self.__dict__)

  def __getitem__(self, key):
    return getattr(self, key)

  def __setitem__(self, key, value):
    return setattr(self, key, value)

  def __contains__(self, key):
    return key in self.__dict__

  def __repr__(self):
    return self.__dict__.__repr__()

