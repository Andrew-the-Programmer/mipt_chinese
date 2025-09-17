import re
import unicodedata

import pypinyin
from dominate import tags

from .dictionary import dictionary
from .html import Html, index


def decode_pinyin(pinyin_type4):
    if not pinyin_type4:
        return ""

    def get_marked(l, tone: int):
        if tone < 1 or tone > 4:
            raise ValueError(f"Invalid tone: {tone}")
        d = {
            ("A", 1): "\u0100",
            ("A", 2): "\u00c1",
            ("A", 3): "\u01cd",
            ("A", 4): "\u00c0",
            ("E", 1): "\u0112",
            ("E", 2): "\u00c9",
            ("E", 3): "\u011a",
            ("E", 4): "\u00c8",
            ("I", 1): "\u012a",
            ("I", 2): "\u00cd",
            ("I", 3): "\u01cf",
            ("I", 4): "\u00cc",
            ("O", 1): "\u014c",
            ("O", 2): "\u00d3",
            ("O", 3): "\u01d1",
            ("O", 4): "\u00d2",
            ("U", 1): "\u016a",
            ("U", 2): "\u00da",
            ("U", 3): "\u01d3",
            ("U", 4): "\u00d9",
            ("a", 1): "\u0101",
            ("a", 2): "\u00e1",
            ("a", 3): "\u01ce",
            ("a", 4): "\u00e0",
            ("e", 1): "\u0113",
            ("e", 2): "\u00e9",
            ("e", 3): "\u011b",
            ("e", 4): "\u00e8",
            ("i", 1): "\u012b",
            ("i", 2): "\u00ed",
            ("i", 3): "\u01d0",
            ("i", 4): "\u00ec",
            ("o", 1): "\u014d",
            ("o", 2): "\u00f3",
            ("o", 3): "\u01d2",
            ("o", 4): "\u00f2",
            ("u", 1): "\u016b",
            ("u", 2): "\u00fa",
            ("u", 3): "\u01d4",
            ("u", 4): "\u00f9",
        }
        return d[(l, tone)]

    vowels = "aeiouAEIOU"

    s = pinyin_type4
    r = ""
    t = ""
    for c in s:
        if re.match("[a-zA-Z]", c):
            t += c
        elif c == ":":
            assert t[-1] == "u"
            t = t[:-1] + "\u00fc"
        elif c >= "0" and c <= "5":
            tone = int(c) % 5
            if tone != 0:
                m = re.search(rf"[{vowels}]+", t)
                if m is None:
                    t += c
                elif len(m.group(0)) == 1:
                    t = t[: m.start(0)] + get_marked(m.group(0), tone) + t[m.end(0) :]
                else:
                    fl = False
                    for cc in "aAoOeE":
                        if cc in t:
                            t = t.replace(cc, get_marked(cc, tone))
                            fl = True
                            break
                    if fl:
                        continue
                    fl = False
                    for cc in ["ui", "Ui", "Iu", "iu"]:
                        if t.endswith(cc):
                            t = t.replace(cc[-1], get_marked(cc[-1], tone))
                            fl = True
                            break
                    if fl:
                        continue
                    t += "!"
        else:
            r += t + c
            t = ""
    r += t
    return r


def get_pinyin(hanzi: str) -> list[list[str]]:
    return pypinyin.pinyin(hanzi, heteronym=True)


def pinyin(hanzi: str) -> Html:
    pyniyin_list = get_pinyin(hanzi)
    text = ""
    for i, pl in enumerate(pyniyin_list):
        if i != 0:
            text += " "
        if len(pl) == 1:
            text += f"{pl[0]}"
        elif len(pl) > 1:
            text += f"[ {' | '.join(pl)} ]"
        else:
            text += "[]"
    return text
