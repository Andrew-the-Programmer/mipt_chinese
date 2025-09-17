from enum import Enum
from typing import Callable

import aqt
from anki.notes import Note
from aqt import Collection
from models import get_model_name
from util import SetFields, SetTags

from hanzi_dict import get_fields, get_tags


def CreateHanziNote(
    hanzi: str,
    funcs: dict[str, Callable[[str], str]] = None,
    col: Collection = aqt.mw.col,
) -> Note:
    mn = get_model_name()
    new_note: Note = col.new_note(col.models.by_name(mn))
    SetFields(new_note, get_fields(hanzi, funcs))
    SetTags(new_note, get_tags(hanzi))
    return new_note


def FindHanziNote(
    hanzi: str, deck_name: str, col: Collection = aqt.mw.col
) -> Note | None:
    note_ids = col.find_notes(f'deck:"{deck_name}" hanzi:"{hanzi}"')
    if len(note_ids) == 0:
        return None
    if len(note_ids) > 1:
        raise RuntimeError(f"Found more than one note for hanzi {hanzi}")
    note = col.get_note(note_ids[0])
    return note
