import warnings
warnings.filterwarnings("ignore")
from .cleaner import cleaner
from .symbols import symbols


# Mappings from symbol to numeric ID and vice versa:
_symbol_to_id = {s: i for i, s in enumerate(symbols)}

def text_to_sequence(text):
  symbols = clean_text(text)
  sequence = symbol_to_sequence(symbols)

  return sequence

def symbol_to_sequence(symbols):
  sequence = []
  for symbol in symbols:
    if symbol not in _symbol_to_id.keys():
      print("{} not in symbol_dict".format(symbol))
      continue
    symbol_id = _symbol_to_id[symbol]
    sequence += [symbol_id]
  
  return sequence

def clean_text(text):
  symbols = cleaner(text)

  return symbols




