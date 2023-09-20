"""Constants used throughout the app.

Constants:
    Page and Section Data:
        PAGE_METADATA: Names of pages using their file names.
        SECTIONS: Language sections in the sidebar.

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

from rich.pretty import pprint

# Page and Section Data ----------------------------------------------------------------
# list of pages to be include in the sidebar.
src_data_dir = Path(__file__).parents[1].joinpath("data")
metadata_filename = "page_metadata.json"

with open(src_data_dir / metadata_filename, "r", encoding="utf-8") as f:
    PAGE_METADATA = json.load(f)

SECTIONS = {
    metadata["section"] for metadata in PAGE_METADATA.values() if metadata["section"]
}


# External Links -----------------------------------------------------------------------
APP_SOURCE_CODE_URL = "https://github.com/cdpeters/portfolio-website"


# Logos and Icons ----------------------------------------------------------------------
ICONS = {
    "github": "/assets/images/github.svg",
    "nav": "/assets/images/bars.svg",
    "section_arrow": "/assets/images/angle-down.svg",
}


# Component IDs ------------------------------------------------------------------------
IDS: dict[str, Any]
# Page link IDs.
IDS = {f"page_{page}": {"link": f"page_{page}_link"} for page in PAGE_METADATA}

# Section IDs.
for section in SECTIONS:
    IDS[f"section_{section}"] = {
        "button": f"section_{section}_button",
        "icon": f"section_{section}_icon",
        "link_div": f"section_{section}_link_div",
    }

# Header IDs.
IDS["header_nav"] = {"button": "header_nav_button", "icon": "header_nav_icon"}

IDS["sidebar"] = "sidebar"
IDS["location"] = "location"


# Frequently Used CSS Classes ----------------------------------------------------------
COLORS = {
    "bg_color_light": "bg-emerald-50",
    "text_color_dark": "text-slate-800",
    "text_color_light": "text-emerald-50",
    "hover_color_dark": "hover:bg-slate-700",
}

if __name__ == "__main__":
    pprint(IDS, indent_guides=False, expand_all=True)
