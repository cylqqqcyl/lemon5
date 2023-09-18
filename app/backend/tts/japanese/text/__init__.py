import warnings
warnings.filterwarnings("ignore")
from .cleaner import cleaner
from .symbols import symbols


# Mappings from symbol to numeric ID and vice versa:
_symbol_to_id = {s: i for i, s in enumerate(symbols)}

def text_to_sequence(text):
  symbols_list = clean_text(text)
  sequence_list = []

  for symbols in symbols_list:
    sequence = []
    for symbol in symbols:
      if symbol not in _symbol_to_id.keys():
        print("{} not in symbol_dict".format(symbol))
        continue
      symbol_id = _symbol_to_id[symbol]
      sequence += [symbol_id]
    sequence_list.append(sequence)

  return sequence_list

def clean_text(text):
  symbols_list = cleaner(text)

  return symbols_list




