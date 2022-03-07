import pathlib
import json
import logging

default = pathlib.Path(__file__).parent / "granita.config.json"
custom = pathlib.Path("granita.config.json")
with open(default) as f:
    data: dict = json.load(f)
if custom.exists():
    logging.info(f"Using custom configuration file {custom.absolute()}")
    with open(custom) as f:
        data.update(json.load(f))
else:
    logging.info(f"Using default configuration file {default.absolute()}")
logging.info("Using configuration:\n" + "\n".join(f"{k}: {v}" for k, v in data.items()))

pages = pathlib.Path(data["pages"])
static = pathlib.Path(data["static"])
public = pathlib.Path(data["public"])
templates = pathlib.Path(data["templates"])
default_template = data["default-template"]
content_selector = data["content-selector"]
extra_data = data["extra-data"]
