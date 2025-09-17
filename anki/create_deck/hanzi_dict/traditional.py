from .dictionary import dictionary


def traditional(hanzi: str) -> str:
    return dictionary.definition_lookup(hanzi)[0]["traditional"]
