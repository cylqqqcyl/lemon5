import re
import unidecode

from natsume import Natsume

"""Japanese characters
"""
_characters = "A-Za-z\d\u3005\u3040-\u30ff\u4e00-\u9faf\uff11-\uff19\uff21-\uff3a\uff41-\uff5a\uff66-\uff9d"
characters_pattern = re.compile(rf"[{_characters}]")

"""Japanese common punctuation marks (full-width and half-width)
Unicode: !?、。！，．？｡､～
ASCII: !?,.~
"""

_common_marks = "\u0021\u003f\u3001\u3002\uff01\uff0c\uff0e\uff1f\uff61\uff64\uff5e"
_common_marks_pattern = re.compile(rf"[{_common_marks}]")

"""Non-Japanese characters and uncommon punctuation marks
"""
_dummy_symbols = f"^{_characters + _common_marks}"
_dummy_symbols_pattern = re.compile(rf"[{_dummy_symbols}]")


_rewrite_symbols = [
    ("sh", "ʃ"),
    ("ch", "ʧ"),
    ("T", "Q"),
    ("ꜜ", "↓"),
    ("ꜛ", "↑")
]

def replace_symbol(symbol, replacement):
    for src, trg in replacement:
        symbol = symbol.replace(src, trg)
    return symbol


_frontend = Natsume()

def cleaner(graphemes):
    graphemes = re.sub(_dummy_symbols_pattern, "", graphemes)   # 去掉无用符号和非日语字符
    sentences = re.split(_common_marks_pattern, graphemes)  # 根据标点讲文本切分成句子
    sentences = list(filter(None, sentences))
    marks = re.findall(_common_marks_pattern, graphemes)
    symbols_list = []

    for i, sentence in enumerate(sentences):
        symbols = _frontend.g2p(sentence, phoneme_mode="romaji", token_mode="phrase", with_accent=True)
        symbols = " ".join(symbols)
        symbols = replace_symbol(symbols, _rewrite_symbols)  # 替换部分音素符号

        # 补上符号
        if i < len(marks):
            mark = unidecode.unidecode(marks[i]).replace(" ", "")
        else:
            mark = ""
        symbols += mark
        symbols_list.append(symbols)
        
    return symbols_list 

