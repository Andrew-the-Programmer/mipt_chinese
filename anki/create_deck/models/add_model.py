import json
import re
from pathlib import Path
from pprint import pprint

import aqt
from anki.models import TemplateDict
from aqt import Collection, mw

from .constants import MODEL_DIR, MODEL_JSON_FILE_NAME

TEMPLATE_JSON = "template.json"
template_fields = ["qfmt", "afmt"]


def get_template(
    template_dir: Path, subs: dict[str, str], col: Collection = aqt.mw.col
) -> TemplateDict:
    def setup_html(html: str):
        for k, v in subs.items():
            html = html.replace("{{" + k + "}}", v)
        return html

    with (template_dir / TEMPLATE_JSON).open("r") as f:
        template_json = json.load(f)

    name = template_json["name"]
    template = col.models.new_template(name)

    def get_field(field_name: str):
        field = template_json.get(field_name, None)
        if field:
            return field
        for f in template_dir.iterdir():
            if f.stem == field_name:
                return f.read_text()
        return ""

    def set_field(field_name: str):
        template[field_name] = get_field(field_name)

    for field_name in template_fields:
        set_field(field_name)

    template["qfmt"] = setup_html(template["qfmt"])
    template["afmt"] = setup_html(template["afmt"])

    return template


def get_templates(model_dir: Path) -> list:
    templates_dir = model_dir / "templates"
    templates = []

    subs: dict[str, str] = {}
    for f in templates_dir.iterdir():
        if f.suffix == ".html":
            subs[f.stem] = f.read_text()

    def is_template_dir(template_dir: Path):
        return (template_dir / TEMPLATE_JSON).exists()

    for template_dir in templates_dir.iterdir():
        if is_template_dir(template_dir):
            templates.append(get_template(template_dir, subs))

    return templates


def update_template(model, template, col: Collection = aqt.mw.col):
    def find_template(name):
        for t in model["tmpls"]:
            if t["name"] == name:
                return t
        return None

    t = find_template(template["name"])
    if t is None:
        col.models.add_template(model, template)
        return

    for field in template_fields:
        t[field] = template[field]


def add_model(model_dir: Path, col: Collection = aqt.mw.col, delete_old=False):
    model_file = model_dir / MODEL_JSON_FILE_NAME
    with model_file.open("r") as field_dict:
        model_json = json.load(field_dict)

    model_name = model_json["name"]
    model = col.models.by_name(model_name)
    if delete_old and model is not None:
        col.models.remove(model["id"])
        model = None
    elif model is None:
        model = col.models.new(model_name)

    # set fields
    old_field_names = set(col.models.field_names(model))

    for index, field in enumerate(model_json["flds"]):
        field_name = field["name"]
        if field_name not in old_field_names:
            col.models.add_field(model, col.models.new_field(field_name))

        # _, field_dict = col.models.field_map(model)[field_name]
        # print(index, field_dict)
        # col.models.moveField(model, field_dict, index)

        if field.get("sort_field", False):
            col.models.set_sort_index(model, index)

    # set style and latex
    with (model_dir / "style.css").open("r") as field_dict:
        model["css"] = field_dict.read()

    with (model_dir / "latex.tex").open("r") as field_dict:
        model["latexPre"], model["latexPost"] = field_dict.read().split("%%%Pre-Post\n")

    # set templates
    templates = get_templates(model_dir)
    for template in templates:
        update_template(model, template)

    col.models.get(model["id"])
    # pprint(model["flds"])
    col.models.save(model)


def add_all_models(col: Collection = aqt.mw.col, **kwargs):
    add_model(MODEL_DIR, col=col, **kwargs)


def main() -> None:
    pprint(get_templates(MODEL_DIR))


if __name__ == "__main__":
    main()
