from dominate import tags

from .html import Html, index, tags


def sound_file(hanzi: str) -> str:
    return f"{hanzi}-sound.mp3"


def sound(hanzi: str) -> Html:
    return f"[sound:{sound_file(hanzi)}]"
