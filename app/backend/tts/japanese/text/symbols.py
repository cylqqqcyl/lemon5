import warnings
warnings.filterwarnings("ignore")

_pad        = '_'
_punctuation = ',.!?~'
_letters = 'AEINOQUabdefghijkmnoprstuvwyzʃʧ↓↑: '

symbols = [_pad] + list(_punctuation) + list(_letters)
