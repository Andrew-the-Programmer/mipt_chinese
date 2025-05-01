import json
from pathlib import Path

import aqt
from aqt import Collection, mw
from col import Note, col
from dominate import tags
from MyUltimateChinese.anki_addon.hanzi_card import CreateHanziNote, FindHanziNote
from MyUltimateChinese.anki_addon.models import get_model_name
from MyUltimateChinese.anki_addon.util import GetField, SetFields
from MyUltimateChinese.hanzi_info import meaning


def update_note(note: Note, word) -> None:
    hanzi = word["hanzi"]
    pinyin = word["pinyin"]
    meaning1 = word["meaning"]
    old_meaning = meaning(hanzi)
    meaning1_html = tags.details(cls="meaning-item", open="")
    with meaning1_html:
        tags.summary("lesson")
        with tags.ul():
            tags.li(meaning1)
    fields = {
        "pinyin": pinyin,
        "meaning": str(meaning1_html) + "\n" + str(old_meaning),
        "front_meaning": meaning1,
    }
    SetFields(note, fields)
    aqt.mw.col.update_note(note)


def main() -> None:
    DECK_NAME = "mipt_chinese::lesson_15::new_words"
    deck_id = aqt.mw.col.decks.id(DECK_NAME)

    new_words_file = (
        Path(__file__).parent.parent / "lessons" / "lesson_15" / "new_words.json"
    )
    with new_words_file.open() as f:
        new_words: list[dict[str, str]] = json.load(f)

    for word in new_words:
        print(word)
        hanzi = word["hanzi"]
        note: Note = FindHanziNote(hanzi, DECK_NAME)
        if note is None:
            note = CreateHanziNote(hanzi)
            aqt.mw.col.add_note(note, deck_id)
            # aqt.mw.col.update_note(note)
            # return
        update_note(note, word)
    # col.save()


if __name__ == "__main__":
    main()
