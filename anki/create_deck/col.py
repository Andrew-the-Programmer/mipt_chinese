import pprint
from pathlib import Path, PurePath

import aqt
import attr
from anki.notes import Note
from aqt import Collection

raise NotImplementedError(
    """
    This script was created for me, to update old notes and add new notes. 
    For that I need to access my collection (local_col), but to create a deck
    you don't need it. So the script needs to be updated. If you really
    want to run this script, put your real ANKI_USER_PATH."
    """
)

ANKI_USER_PATH = Path.home() / Path(".local/share/Anki2/Me")

ANKI_MEDIA_PATH = ANKI_USER_PATH / "collection.media"

local_col = Collection(path=ANKI_USER_PATH / "collection.anki2")


@attr.define()
class MW:
    col: Collection = attr.field()


aqt.mw = MW(local_col)
