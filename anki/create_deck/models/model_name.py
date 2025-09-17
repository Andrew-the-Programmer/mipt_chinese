import json
from pathlib import Path

from .constants import MODEL_DIR, MODEL_JSON_FILE_NAME


def get_model_name():
    model_dir = MODEL_DIR
    model_file = model_dir / MODEL_JSON_FILE_NAME
    with model_file.open("r") as f:
        return json.load(f)["name"]
