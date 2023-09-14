"""Constants used throughout the app.

A `secrets.toml` file is loaded via the `tomli` library and the appropriate constants
are assigned. Additional constants (not contained within `secrets.toml`) are also
defined.

Constants:
    Names:
        PAGE_METADATA: Names of pages using their file names.

    Data Directories:
        GOOGLE_DRIVE_DIR: Path to shared google drive collaboration folder.
        DATA_DIR: Path to the `data` directory in the project root (`dash-test-app`).

    External Links:
        APP_SOURCE_CODE_URL

    Logos and Icons:
        ICONS

    Component IDs:
        IDS

    Frequently Used CSS Classes:
        COLORS
"""
import json
from pathlib import Path
from typing import Any

import tomli
from rich.pretty import pprint

# list of pages to be include in the sidebar.
src_data_dir = Path(__file__).parents[1].joinpath("data")

with open(src_data_dir / "page_metadata.json") as f:
    PAGE_METADATA = json.load(f)

SECTIONS = {
    metadata["section"] for metadata in PAGE_METADATA.values() if metadata["section"]
}

# Load secrets.toml --------------------------------------------------------------------
# Use the file path (`__file__`) of this module to form the paths to both the google
# drive collaboration folder and to the project's data directory. `parents[2]` is the
# 3rd parent (since index 2 is 3rd element) of the file path for this module: the
# project's root directory `dash-test-app`.
GOOGLE_DRIVE_DIR: Path | None
try:
    with open(Path(__file__).parents[2] / "secrets.toml", "rb") as f:
        secrets = tomli.load(f)
    GOOGLE_DRIVE_DIR = Path(secrets["google_drive"]["path"])
except FileNotFoundError:
    GOOGLE_DRIVE_DIR = None


# Data Directories ---------------------------------------------------------------------
DATA_DIR = Path(__file__).parents[2] / "data"


# External Links -----------------------------------------------------------------------
APP_SOURCE_CODE_URL = "https://github.com/cdpeters/portfolio-website"


# Logos and Icons ----------------------------------------------------------------------
ICONS = {
    "github": "/assets/images/github.svg",
    "nav": "/assets/images/compass.svg",
    "section_arrow": "/assets/images/angle-down.svg",
}


# Component IDs ------------------------------------------------------------------------
# Page IDs.
IDS: dict[str, Any]
IDS = {f"page_{page}": {"link": f"page_{page}_link"} for page in PAGE_METADATA}

for section in SECTIONS:
    IDS[f"section_{section}"] = {
        "button": f"section_{section}_button",
        "icon": f"section_{section}_icon",
        "link_div": f"section_{section}_link_div",
    }

IDS["header_nav"] = {"button": "header_nav_button", "icon": "header_nav_icon"}

IDS["sidebar"] = "sidebar"
IDS["location"] = "location"
IDS["figure_bar"] = "figure_bar"
IDS["figure_temp"] = "figure_temp"
IDS["figure_precip"] = "figure_precip"
IDS["table_climate"] = "table_climate"


# Frequently Used CSS Classes ----------------------------------------------------------
COLORS = {
    "bg_color_prefix": "bg",
    "bg_color_dark": "bg-slate-800",
    "bg_color_light": "bg-emerald-50",
    "text_color_prefix": "text",
    "text_color_dark": "text-slate-800",
    "text_color_light": "text-emerald-50",
    "hover_color_dark": "hover:bg-slate-700",
}

if __name__ == "__main__":
    print("")
    # pprint(PAGE_METADATA["home"]["section"], indent_guides=False, expand_all=True)
    pprint(IDS, indent_guides=False, expand_all=True)
