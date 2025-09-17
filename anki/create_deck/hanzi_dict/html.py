from dominate import tags
from dominate.tags import html_tag

type Html = html_tag


def index(cls: str, *args, **kwargs) -> Html:
    return tags.div(*args, cls=cls, **kwargs)


def ul_tag(l: list[str]) -> Html:
    res = tags.ul()
    with res:
        for item in l:
            tags.li(item)
    return res


def audio_tag(src: str) -> Html:
    return tags.span(f"[sound:{src}]", cls="sound")


def details_tag(summary: str) -> Html:
    with index(summary):
        d = tags.details()
        with d:
            tags.summary(summary)
            return d
