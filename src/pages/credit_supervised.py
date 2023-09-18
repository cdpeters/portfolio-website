"""Layout for the background page.

Displays an example project background using markdown.

Variables:
    markdown
    layout
"""
from pathlib import Path

from dash import dcc, html, register_page

from utils.constants import IDS, PAGE_METADATA
from utils.project_page_constants import LAYOUT, SUMMARY_BAR, SUMMARY_DATA, SUMMARY_KEYS

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
# Summary section.
summary_data = list()
for key in SUMMARY_KEYS:
    # Header metadata values that are None will be assigned "N/A" instead.
    if not page_metadata[key]:
        page_metadata[key] = "N/A"

    # label_div.
    label_div = html.Div(
        SUMMARY_DATA[key]["label_div"]["label"],
        className=SUMMARY_DATA[key]["label_div"]["class"],
    )
    summary_data.append(label_div)

    # data_div.
    data_div = html.Div(
        page_metadata[key],
        className=SUMMARY_DATA[key]["data_div"]["class"],
    )
    summary_data.append(data_div)

summary = html.Div(
    [
        # Summary title bar.
        html.Div(
            [
                # Summary title bar label.
                html.Div(
                    SUMMARY_BAR["div"]["label"], className=SUMMARY_BAR["div"]["class"]
                ),
                # Repo link.
                dcc.Link(
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
                    refresh=True,
                    target="_blank",
                    className=SUMMARY_BAR["link"]["class"],
                ),
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

markdown = dcc.Markdown(
    markdown_contents,
    link_target="_blank",
    dangerously_allow_html=True,
)

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
