from .html import Html, tags
from .meaning import get_meaning


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
