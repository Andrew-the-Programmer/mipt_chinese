import json
from pathlib import Path
from typing import Self

from col import Collection, local_col
from dominate import tags
from hanzi_dict import get_fields as get_dict_fields
from hanzi_dict.components import get_components_all
from hanzi_dict.meaning import meaning as get_dict_meaning
from hanzi_dict.strokes import strokes as get_dict_strokes
from hanzi_note import CreateHanziNote, FindHanziNote
from models import add_all_models, get_model_name
from typ import Note
from util import GetField, SetFields


class WordDict(dict):
    pass


class DeckDict(dict):
    parent: Self = None

    def __init__(
        self,
        deck_dict: dict,
        *,
        parent: Self | str | list[str] = None,
        name=None,
        children: list = None,
        notes: list = None,
        full_name=None,
    ):
        self |= deck_dict

        if name is not None:
            self["name"] = name
        if children is not None:
            self["children"] = children
        if notes is not None:
            self["notes"] = notes

        if isinstance(parent, DeckDict):
            self.parent = parent
        if isinstance(parent, list):
            if len(parent) > 0:
                self.parent = DeckDict({}, parent=parent[:-1], name=parent[-1])
        if isinstance(parent, str):
            self.parent = DeckDict({}, parent=parent.split("::"))
        if full_name is not None:
            split = full_name.split("::")
            self.__init__({}, parent=split[:-1], name=split[-1])

    def Children(self) -> list:
        if "children" not in self:
            return []
        for deck_dict in self["children"]:
            yield DeckDict(deck_dict, parent=self)

    def Notes(self) -> list[WordDict]:
        return self.get("notes", [])

    def Name(self) -> str:
        return self["name"]

    def FullName(self) -> str:
        if self.parent is None:
            return self.Name()
        return self.parent.FullName() + "::" + self.Name()


def get_index(deck_dict: DeckDict, suffix: str) -> str:
    return deck_dict.FullName().split("::", 1)[-1] + "::" + suffix


def update_note(note: Note, word: WordDict) -> None:
    hanzi = word["hanzi"]
    pinyin = word["pinyin"]
    lesson_meaning = word["meaning"]
    order_in_lesson = word["order_in_lesson"]
    dict_meaning = get_dict_meaning(hanzi)
    lesson_meaning_html = tags.details(cls="meaning-item", open="")
    with lesson_meaning_html:
        tags.summary("lesson")
        with tags.ul():
            tags.li(lesson_meaning)
    fields = {
        "pinyin": pinyin,
        "order_in_lesson": order_in_lesson,
        "meaning": str(lesson_meaning_html) + "\n" + str(dict_meaning),
        "front_meaning": lesson_meaning,
    }
    SetFields(note, fields)


components: dict[str, list[str]] = {}


def prepare_links(deck_dict: str, word_hanzi: str):
    new_component = get_index(deck_dict, word_hanzi)

    def f(hanzi: str) -> None:
        if hanzi not in components:
            components[hanzi] = []
        if new_component not in components[hanzi]:
            components[hanzi].append(new_component)

    return f


def get_links(hanzi: str):
    d = components.get(hanzi, [])
    res = tags.ol()
    with res:
        for c in d:
            tags.li(c)
    return str(res)


def add_word(
    deck_dict: DeckDict,
    word_dict: WordDict,
    word_order_in_lesson: int,
    col: Collection = None,
) -> None:
    deck_fullname = deck_dict.FullName()
    word_dict["order_in_lesson"] = get_index(deck_dict, str(word_order_in_lesson))
    if "hanzi" not in word_dict:
        raise ValueError
    hanzi = word_dict["hanzi"]
    if isinstance(hanzi, list):
        hanzi = word_dict["hanzi"] = ", ".join(hanzi)
    note = FindHanziNote(hanzi, deck_fullname, col=col)
    funcs = {"links": get_links}
    if note is None:
        note = CreateHanziNote(hanzi, funcs, col=col)
        col.add_note(note, col.decks.id(deck_fullname))
    update_note(note, word_dict)
    col.update_note(note)


def prepare_word(
    deck_dict: DeckDict,
    word_dict: WordDict,
    word_order_in_lesson: int,
    col: Collection = None,
) -> None:
    if isinstance(word_dict["hanzi"], list):
        # print(word_dict["hanzi"])
        for subword in word_dict["hanzi"]:
            subword_dict = word_dict.copy()
            subword_dict["hanzi"] = subword
            prepare_word(
                deck_dict,
                subword_dict,
                word_order_in_lesson,
                col=col,
            )
            return

    hanzi = word_dict["hanzi"]
    all_components = get_components_all(hanzi)
    func = prepare_links(deck_dict, hanzi)
    for c in all_components:
        func(c)


def prepare_deck(deck_dict: DeckDict, col: Collection = None) -> None:
    full_deck_name = DeckDict.FullName(deck_dict)
    print(full_deck_name)
    for child_deck_dict in DeckDict.Children(deck_dict):
        prepare_deck(
            child_deck_dict,
            col=col,
        )

    for index, word in enumerate(DeckDict.Notes(deck_dict)):
        prepare_word(
            deck_dict,
            word,
            word_order_in_lesson=index,
            col=col,
        )


def add_deck(deck_dict: DeckDict, col: Collection = None) -> None:
    full_deck_name = DeckDict.FullName(deck_dict)
    print(full_deck_name)
    for child_deck_dict in DeckDict.Children(deck_dict):
        add_deck(
            child_deck_dict,
            col=col,
        )

    for index, word in enumerate(DeckDict.Notes(deck_dict)):
        add_word(
            deck_dict,
            word,
            word_order_in_lesson=index,
            col=col,
        )


def add_new_words(new_words_json_file, col: Collection = None) -> None:
    with new_words_json_file.open() as f:
        deck_dict = DeckDict(json.load(f))

    prepare_deck(deck_dict, col=col)
    add_deck(deck_dict, col=col)


def main():
    add_all_models(delete_old=True, col=local_col)
    new_words_file = Path("new_words.json")
    add_new_words(new_words_file, col=local_col)


if __name__ == "__main__":
    main()
