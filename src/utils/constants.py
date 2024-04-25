"""Constants used throughout the app.

Constants:
    Page and Section Data:
        PAGE_METADATA: Names of pages using their file names.
        SECTIONS: Language sections in the sidebar.

    External Links:
        EXTERNAL_LINKS

    Logos and Icons:
        ICONS

    Images
        IMAGES

    Component IDs:
        IDS

    Frequently Used CSS Classes:
        COLORS
"""
import json
from pathlib import Path
from typing import Any

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
EXTERNAL_LINKS = {
    "portfolio": "https://github.com/cdpeters/portfolio-website",
    "github": "https://github.com/cdpeters",
    "linkedin": "https://www.linkedin.com/in/cdpeters1/",
    "email": "mailto:cdpeters1@gmail.com",
    "resume": "https://drive.google.com/file/d/10KNwUkqPCGEODEX5FX-jDgbw_LM_ip_i/view?usp=sharing",
}


# Logos and Icons ----------------------------------------------------------------------
ICONS = {
    "github_light": "/assets/images/github_light.svg",
    "github_dark": "/assets/images/github_dark.svg",
    "linkedin": "/assets/images/linkedin.svg",
    "email": "/assets/images/envelope.svg",
    "resume": "/assets/images/file-lines.svg",
    "nav": "/assets/images/bars.svg",
    "section_arrow": "/assets/images/angle-down.svg",
}


# Images -------------------------------------------------------------------------------
IMAGES = {
    "face": "/assets/images/profile_picture_square.jpg",
    "galaxy": "/assets/images/galaxy.jpg",
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
