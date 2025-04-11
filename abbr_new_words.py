import json
import re


def load_chinese(json_file):
    with open(json_file, "r", encoding="utf-8") as f:
        return json.load(f)


def get_abbreviations(chinese_words):
    return {
        word["Hanzi"]: f"{word['Pinyin']} - {word['Meaning']}" for word in chinese_words
    }


def replace_words(text, abbreviations):
    pattern = re.compile(
        "|".join(re.escape(key) for key in abbreviations.keys()), re.UNICODE
    )

    def replacement(match):
        abbr = abbreviations[match.group(0)]
        return f"<abbr title='{abbr}'>{match.group(0)}</abbr>"

    return pattern.sub(replacement, text)


def main():
    json_file = "chinese_words.json"
    text_file = "input.md"
    output_file = "output.md"

    chinese_words = load_chinese(json_file)
    abbreviations = get_abbreviations(chinese_words)

    with open(text_file, "r", encoding="utf-8") as f:
        text = f.read()

    replaced_text = replace_words(text, abbreviations)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(replaced_text)

    print(f"Replacement completed. Output saved to '{output_file}'.")


if __name__ == "__main__":
    main()
