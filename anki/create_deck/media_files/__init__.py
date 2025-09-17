import json
from pathlib import Path
from shutil import copy

from aqt import mw

from ..hanzi_note.get_fields.components import get_all_components

LOCAL_MEDIA_DIR = Path(__file__).parent / "media"


def add_media_file(file: Path):
    ANKI_MEDIA_DIR = Path(mw.pm.profileFolder()) / "collection.media"
    ANKI_MEDIA_DIR.mkdir(parents=True, exist_ok=True)
    copy(file, ANKI_MEDIA_DIR / file.name)


def add_all_media_files():
    for media_file in LOCAL_MEDIA_DIR.iterdir():
        add_media_file(media_file)


def add_media_files_for_hanzi(hanzi: str):
    all_components = get_all_components(hanzi)
    for media_file in LOCAL_MEDIA_DIR.iterdir():
        if any([media_file.name.startswith(c) for c in all_components]):
            add_media_file(media_file)
