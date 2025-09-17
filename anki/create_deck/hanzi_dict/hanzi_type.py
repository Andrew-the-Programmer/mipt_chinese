from enum import Enum, auto

from dominate import tags
from hanzipy.exceptions import NotAHanziCharacter

from .dictionary import decomposer, dictionary
from .html import Html, index


class HanziType(Enum):
    GRAPHICAL = auto()
    RADICAL = auto()
    WORD = auto()
    SENTENCE = auto()
    UNKNOWN = auto()


def get_hanzi_type(hanzi: str):
    if hanzi in decomposer.radicals:
        return HanziType.RADICAL
    try:
        dictionary.definition_lookup(hanzi)
        return HanziType.WORD
    except KeyError:
        return HanziType.SENTENCE
    except NotAHanziCharacter:
        if decomposer.component_exists(hanzi):
            return HanziType.GRAPHICAL
        return HanziType.UNKNOWN


def hanzi_type(hanzi: str) -> Html:
    ht = get_hanzi_type(hanzi)
    return ht.name
