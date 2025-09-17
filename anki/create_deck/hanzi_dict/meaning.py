import html

import dominate
import zhon
from dominate import tags
from hanzipy.exceptions import NotAHanziCharacter
from pypinyin.tools.toneconvert import convert

from .dictionary import decomposer, dictionary
from .hanzi_type import HanziType, get_hanzi_type
from .html import Html, details_tag, index, ul_tag
from .pinyin import decode_pinyin


def get_meaning(hanzi: str) -> list[dict[str, list[str]]]:
    hanzi_type = get_hanzi_type(hanzi)
    match hanzi_type:
        case HanziType.RADICAL:
            return [{"definition": decomposer.get_radical_meaning(hanzi).split("/")}]
        case HanziType.WORD:
            return [
                {
                    "summary": decode_pinyin(d["pinyin"]),
                    "definition": d["definition"].split("/"),
                }
                for d in dictionary.definition_lookup(hanzi)
            ]

        case HanziType.GRAPHICAL:
            return []

        case HanziType.SENTENCE:
            return []
            # raise NotImplementedError(f"Sentences not supported yet: {hanzi}")
        case HanziType.UNKNOWN:
            return []
            # raise ValueError(f"Invalid hanzi: {hanzi}")
    raise ValueError("Unreachable")


def front_meaning(hanzi: str) -> Html:
    ml = get_meaning(hanzi)
    res = tags.ul()
    with res:
        for m in ml:
            d = m["definition"]
            if len(d) == 0:
                continue
            tags.li(" , ".join(d), cls="meaning-item")
    return res


def meaning(hanzi: str) -> str:
    ml = get_meaning(hanzi)
    k = 1
    res_list = []
    for m in ml:
        p = m.get("summary", None)
        d = m["definition"]
        if len(d) == 0:
            continue
        if p is None:
            p = str(k)
            k += 1
        item = tags.details(open="", cls="meaning-item")
        with item:
            tags.summary(p)
            ul_tag(d)
        res_list.append(str(item))
    return "\n".join(res_list)
