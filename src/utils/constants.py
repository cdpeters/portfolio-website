"""Constants used throughout the app.

A `secrets.toml` file is loaded via the `tomli` library and the appropriate constants
are assigned. Additional constants (not contained within `secrets.toml`) are also
defined.

Constants:
    Names:
        SIDEBAR_PAGE_NAMES

    Data Directories:
        GOOGLE_DRIVE_DIR: Path to shared google drive collaboration folder.
        DATA_DIR: Path to the `data` directory in the project root (`dash-test-app`).

    External Links:
        APP_SOURCE_CODE_URL

    Logos and Icons:
        ICONS

    Frequently Used CSS Classes:
        COLORS

    Component IDs:
        IDS
"""

from pathlib import Path
from typing import Any

import tomli

# list of pages to be include in the sidebar.
SIDEBAR_PAGE_NAMES = ("home", "background", "handbell_music", "dashboard", "another")


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
ICONS = {"github": "/assets/images/github.svg"}


# Component IDs ------------------------------------------------------------------------
# Page IDs.
IDS: dict[str, Any]
IDS = {
    page: {
        "link": f"{page}_link",
    }
    for page in SIDEBAR_PAGE_NAMES
}

IDS["figure_bar"] = "figure_bar"
IDS["figure_temp"] = "figure_temp"
IDS["figure_precip"] = "figure_precip"
IDS["location"] = "location"
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
