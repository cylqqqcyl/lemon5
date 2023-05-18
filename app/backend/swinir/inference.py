import cv2
import numpy as np
import torch
import shutil
from network_swinir import SwinIR as net
import os

# global variables
source_path = ''
flag_upload = False     # 等待输入source path
flag_generate = False   # 是否等待启动generate
flag_terminate = False  # 是否结束线程
device = torch.device('cpu')    # 仅支持CPU推理


class SwinIR:
    def __init__(self, model_path):
        self.model_path = model_path
        self.save_path = 'cache/swinir_generated.png'
        self.display_path = 'cache/swinir_display.png'
        self.download_path = 'cache/swinir_download.png'

        self.scale = 4
        self.border = 0
        self.window_size = 8

        self.load_model()

    def load_model(self):
        # define model
        model = net(upscale=self.scale, in_chans=3, img_size=64, window_size=8,
                    img_range=1., depths=[6, 6, 6, 6, 6, 6], embed_dim=180, num_heads=[6, 6, 6, 6, 6, 6],
                    mlp_ratio=2, upsampler='nearest+conv', resi_connection='1conv')
        param_key_g = 'params_ema'
        # load model
        # print(f'Loading model from {self.model_path}...')
        pretrained_model = torch.load(self.model_path)
        model.load_state_dict(
            pretrained_model[param_key_g] if param_key_g in pretrained_model.keys() else pretrained_model, strict=True)

        model.eval()
        model = model.to(device)
        # print('Successfully loaded SwinIR model!')
        self.model = model

    def inference(self, img_path):
        img_lq = cv2.imread(img_path, cv2.IMREAD_COLOR).astype(np.float32) / 255.

        img_lq = np.transpose(img_lq if img_lq.shape[2] == 1 else img_lq[:, :, [2, 1, 0]],
                              (2, 0, 1))  # HCW-BGR to CHW-RGB
        img_lq = torch.from_numpy(img_lq).float().unsqueeze(0).to(device)  # CHW-RGB to NCHW-RGB

        # inference
        with torch.no_grad():
            # pad input image to be a multiple of window_size
            _, _, h_old, w_old = img_lq.size()
            h_pad = (h_old // self.window_size + 1) * self.window_size - h_old
            w_pad = (w_old // self.window_size + 1) * self.window_size - w_old
            img_lq = torch.cat([img_lq, torch.flip(img_lq, [2])], 2)[:, :, :h_old + h_pad, :]
            img_lq = torch.cat([img_lq, torch.flip(img_lq, [3])], 3)[:, :, :, :w_old + w_pad]
            output = self.model(img_lq)

            output = output[..., :h_old * 4, :w_old * self.scale]

        output = output.data.squeeze().float().cpu().clamp_(0, 1).numpy()
        if output.ndim == 3:
            output = np.transpose(output[[2, 1, 0], :, :], (1, 2, 0))  # CHW-RGB to HCW-BGR
        output = (output * 255.0).round().astype(np.uint8)  # float32 to uint8
        cv2.imwrite(self.save_path, output)
        shutil.copy(self.save_path, self.display_path)
        shutil.copy(self.save_path, self.download_path)

def wait_upload():
    global flag_upload
    while True:
        if flag_upload:
            break


def load_image(image_path):
    global source_path
    global flag_upload
    if image_path:
        source_path = image_path
        flag_upload = True


def wait_generate():
    global flag_generate
    while True:
        if flag_generate:
            break


def generate_image():
    global flag_upload, flag_generate, source_path
    if source_path:
        flag_upload = True
        flag_generate = True

def terminate_sr():
    global flag_upload, flag_terminate
    flag_terminate = True
    flag_upload = True

def revise_path(origin_path):
    origin_path = origin_path.replace('\\', '/').replace('\n', '/n').replace('\r', '/r')
    revised_path = origin_path.replace('\t', '/t').replace('\a', '/a').replace('\b', '/b')

    return revised_path



def super_resolution(model_dir):
    print('Lemon4> Begin image super resolution!')
    model_path = os.path.join(model_dir, 'model.pth')
    print('Lemon4> Loading models...')
    swinir = SwinIR(model_path)
    print('Lemon4> Successfully loaded model!')

    while True:
        global flag_upload, flag_generate, flag_terminate, source_path
        flag_upload = flag_generate = flag_terminate = False

        print('Lemon4> Please input some images...')
        wait_upload()

        if flag_terminate:
            print('Lemon4> Terminating...')
            break

        source_path = revise_path(source_path)
        print(f'Lemon4> Successfully loaded image from {source_path}')

        wait_generate()

        print('Lemon4> Generating image...')
        try:
            swinir.inference(source_path)
            print('Lemon4> Successfully generated restored image!')
        except Exception as e:
            print(e)

    print('Lemon4> Super resolution is terminated!')


if __name__ == '__main__':
    # debug use
    image_path = '../../cache/sample_input/chip.png'    # 输入图片路径
    model_dir = '../../swinir'

    model_path = os.path.join(model_dir, 'model.pth')     # 模型文件路径
    swinir = SwinIR(model_path)
    swinir.inference(image_path)

