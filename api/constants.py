import json

CHINESE_WORD_NOTE_TYPE: dict[str, object] = {}

with open("api/chinese_word_note_type.json") as f:
    CHINESE_WORD_NOTE_TYPE = json.load(f)

CHINESE_WORD_NOTE_TYPE_ID = CHINESE_WORD_NOTE_TYPE["originalId"]

SOURCE_DECK_NAME = "Ultimate Chinese::1. Ultimate Characters"
