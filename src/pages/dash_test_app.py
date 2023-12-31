"""Layout for each project page.

Displays a project summary (via the page's metadata) along with the given project's
README.md markdown.

Variables:
    layout
"""
from pathlib import Path

from dash import dcc, html, register_page

from utils.constants import IDS, PAGE_METADATA
from utils.project_page_constants import (
    LAYOUT,
    MARKDOWN,
    SUMMARY_BAR,
    SUMMARY_DATA,
    SUMMARY_KEYS,
)

# Extract page name from the module name.
page = __name__.replace("pages.", "")
page_metadata = PAGE_METADATA[page].copy()

# Register page ------------------------------------------------------------------------
register_page(__name__, **page_metadata, id_page_link=IDS[f"page_{page}"]["link"])

# Read markdown file -------------------------------------------------------------------
pages_markdown_dir = Path(__file__).parents[1].joinpath("pages_markdown")
# Read the markdown file associated with this page in as string.
with open(pages_markdown_dir / f"{page}.md", "r", encoding="utf-8") as f:
    markdown_contents = f.read()

# Create page layout -------------------------------------------------------------------
# Outline:
#   Build project summary data pieces
#   Build the summary section that shows at the top of the page
#   Build the project's README markdown component
#   Assemble the page in the variable `layout`

# Build project summary data pieces.
summary_data = list()
for key in SUMMARY_KEYS:
    # Summary data values that are None will be assigned "N/A" instead.
    if not page_metadata[key]:
        page_metadata[key] = "N/A"

    # Label div.
    label_div = html.Div(
        SUMMARY_DATA[key]["label_div"]["label"],
        className=SUMMARY_DATA[key]["label_div"]["class"],
    )
    summary_data.append(label_div)

    # Data div.
    if (key == "website") and (page_metadata[key] != "N/A"):
        data_div = html.Div(
            dcc.Link(
                page_metadata["website_name"], href=page_metadata[key], target="_blank"
            ),
            className=SUMMARY_DATA[key]["data_div"]["class"],
        )
    else:
        data_div = html.Div(
            page_metadata[key],
            className=SUMMARY_DATA[key]["data_div"]["class"],
        )
    summary_data.append(data_div)

# Summary title bar label.
summary_title_bar_label = html.Div(
    SUMMARY_BAR["div"]["label"], className=SUMMARY_BAR["div"]["class"]
)

# Repo link.
repo_link = dcc.Link(
    [
        html.Img(
            src=SUMMARY_BAR["img"]["src"],
            className=SUMMARY_BAR["img"]["class"],
        ),
        html.Span(
            SUMMARY_BAR["span"]["label"],
            className=SUMMARY_BAR["span"]["class"],
        ),
    ],
    href=page_metadata["repo"],
    target="_blank",
    className=SUMMARY_BAR["link"]["class"],
)

# Build the summary section that shows at the top of the page.
summary = html.Div(
    [
        # Summary title bar.
        html.Div(
            [
                summary_title_bar_label,
                repo_link,
            ],
            className=SUMMARY_BAR["class"],
        ),
        # Summary data.
        html.Div(
            summary_data,
            className=SUMMARY_DATA["class"],
        ),
    ],
)

# Build the project's README markdown component.
markdown = dcc.Markdown(
    markdown_contents,
    link_target="_blank",
    dangerously_allow_html=True,
    mathjax=True,
    className=MARKDOWN["class"],
)

# Assemble the page in the variable `layout`.
layout = html.Div(
    # Prose container.
    html.Div(
        [
            summary,
            html.Hr(className=LAYOUT["hr"]["class"]),
            markdown,
        ],
        className=LAYOUT["div"]["class"],
    ),
    className=LAYOUT["class"],
)
