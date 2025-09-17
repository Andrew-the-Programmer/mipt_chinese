from dominate import tags

from .components import get_components
from .hanzi_type import HanziType, get_hanzi_type
from .html import Html


def strokes_file(hanzi: str) -> str:
    return f"{hanzi}-strokes.gif"


def strokes(hanzi: str) -> Html:
    res = tags.div()
    with res:
        hanzi_type = get_hanzi_type(hanzi)
        if len(hanzi) > 1 and hanzi_type == HanziType.WORD:
            for symbol in get_components(hanzi):
                tags.img(cls="animated-gif", src=strokes_file(symbol))
        elif len(hanzi) == 1:
            tags.img(cls="animated-gif", src=strokes_file(hanzi))
    return res
