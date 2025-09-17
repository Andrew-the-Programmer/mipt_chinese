from get_fields import get_fields
from get_fields.dictionary import *
from get_fields.frequency import frequency
from get_fields.meaning import *
from wordfreq import word_frequency


def info_html() -> str:
    with open("info.html", "r") as f:
        return f.read()


def get_info(hanzi: str) -> str:
    fields = get_fields(hanzi)
    info = info_html()

    for k, v in fields.items():
        info = info.replace("{{" + k + "}}", str(v))

    return info


def main() -> None:
    print(frequency("案件"))
    hanzi = "刷"
    print(meaning(hanzi))
    # with open(f"{hanzi}.html", "w") as f:
    #     f.write(get_info(hanzi))


if __name__ == "__main__":
    main()
