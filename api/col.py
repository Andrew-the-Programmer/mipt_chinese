import pprint
from pathlib import Path, PurePath

import aqt
import attr
from anki.notes import Note
from aqt import Collection

ANKI_USER_PATH = Path.home() / Path(".local/share/Anki2/Me")

col = Collection(path=ANKI_USER_PATH / "collection.anki2")


@attr.define()
class MW:
    col: Collection = attr.field()


aqt.mw = MW(col)
