from collections.abc import Iterable

import jieba

from .dictionary import chin_dict, decomposer
from .hanzi_type import HanziType, get_hanzi_type

# a special value in dict
NOTHING = "No glyph available"


def _get_decomposition(hanzi: str) -> dict[str, set[str]]:
    d = decomposer.decompose(hanzi)
    d.pop("character")
    res: dict[str, set[str]] = {k: set(v) for k, v in d.items()}
    for k in res:
        res[k].discard(NOTHING)
        res[k].discard(hanzi)
    return res


def _get_graphical_decomposition(hanzi: str) -> set[str]:
    return _get_decomposition(hanzi)["graphical"]


def _get_radical_decomposition(hanzi: str) -> set[str]:
    return _get_decomposition(hanzi)["radical"]


def _get_once_decomposition(hanzi: str) -> set[str]:
    return _get_decomposition(hanzi)["once"]


def _get_all_components(hanzi: str) -> set[str]:
    decomposition = _get_decomposition(hanzi)
    res = set()
    once: set[str] = decomposition["once"]
    radical: set[str] = decomposition["radical"]
    graphical: set[str] = decomposition["graphical"]

    un = once | radical | graphical

    for o in un:
        res.update(_get_all_components(o))

    res.update(un)
    res.add(hanzi)

    return res


def get_components(hanzi: str) -> list[str]:
    hanzi_type = get_hanzi_type(hanzi)

    res = set()
    answer: list[str] = []

    def append(c: str):
        if c not in res:
            res.add(c)
            answer.append(c)

    def update(cc: Iterable[str]):
        for c in cc:
            append(c)

    # print(hanzi, hanzi_type)

    match hanzi_type:
        case HanziType.GRAPHICAL | HanziType.RADICAL:
            decomposition = _get_decomposition(hanzi)
            once: set[str] = decomposition["once"]
            update(once)
            graphical: set[str] = decomposition["graphical"]
            once_graphical = set()
            for o in once:
                once_graphical.update(_get_graphical_decomposition(o))
            for g in graphical:
                if g not in once_graphical:
                    append(g)

        case HanziType.WORD:
            jieba_components = list(jieba.cut(hanzi))
            if len(jieba_components) > 1:
                return jieba_components

            if len(hanzi) > 1:
                return list(hanzi)

            decomposition = _get_decomposition(hanzi)
            once: set[str] = decomposition["once"]
            radical: set[str] = decomposition["radical"]
            graphical: set[str] = decomposition["graphical"]
            all_components: set[str] = set()
            res.update(once)
            for o in once:
                all_components.update(_get_all_components(o))
            for r in radical:
                if r not in all_components:
                    res.add(r)
            for r in radical:
                all_components.update(_get_all_components(r))
            for g in graphical:
                if g not in all_components:
                    res.add(g)

        case HanziType.SENTENCE:
            jc = list(jieba.cut(hanzi))
            if len(jc) > 1:
                return [c for c in jc if get_hanzi_type(c) != HanziType.UNKNOWN]
            if len(hanzi) > 1:
                return list(hanzi)
            # raise NotImplementedError(f"Sentences not supported yet: {hanzi}")

        case HanziType.UNKNOWN:
            pass
            # raise ValueError(f"Invalid hanzi: {hanzi}")

    return list(res)


def get_components_all(hanzi: str) -> list[str]:
    components = get_components(hanzi)
    for c in components:
        components.extend(get_components_all(c))
    return components
