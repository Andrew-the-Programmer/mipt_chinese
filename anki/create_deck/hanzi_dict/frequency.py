from wordfreq import word_frequency

from .dictionary import dictionary


def frequency(hanzi: str) -> str:
    try:
        # return str(dictionary.get_character_frequency(hanzi)["number"])
        return f"{word_frequency(hanzi, "zh") * 100:.2g}%"
    except:
        return "0"
