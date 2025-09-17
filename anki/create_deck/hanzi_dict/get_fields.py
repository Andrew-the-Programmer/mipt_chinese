import re
from collections.abc import Callable
from pathlib import Path

from bs4 import BeautifulSoup
from dominate import tags

from .components import get_components
from .frequency import frequency
from .front_meaning import front_meaning
from .hanzi_type import hanzi_type
from .hints import hints as front_hints
from .html import Html
from .meaning import meaning
from .notes import notes
from .pinyin import pinyin
from .sound import sound
from .strokes import strokes


def get_components_html(
    hanzi: str, funcs: dict[str, Callable[[str], str]] = None
) -> Html:
    cs: list["hanzi"] = get_components(hanzi)
    res = tags.div()
    for c in cs:
        c_html = get_component_html(c, funcs)
        res.add_raw_string(c_html)
    return res


def get_component_html(
    hanzi: str, funcs: dict[str, Callable[[str], str]] = None
) -> Html:
    info_file = Path(__file__).parent / "component.html"
    with info_file.open("r") as f:
        info_html = f.read()

    fields = get_fields(hanzi, funcs)

    for k, v in fields.items():
        info_html = info_html.replace("{{" + k + "}}", str(v))

    return info_html


def get_fields(
    hanzi: str, funcs: dict[str, Callable[[str], str]] = None
) -> dict[str, str]:
    res = {
        "hanzi": hanzi,
        "pinyin": pinyin(hanzi),
        "hanzi_type": hanzi_type(hanzi),
        "sound": sound(hanzi),
        "strokes": strokes(hanzi),
        "meaning": meaning(hanzi),
        "components": get_components_html(hanzi, funcs),
        "front_meaning": front_meaning(hanzi),
        "front_hints": front_hints(hanzi),
        "notes": notes(hanzi),
        "frequency": frequency(hanzi),
    }
    for k, v in funcs.items():
        res[k] = v(hanzi)
    return res
