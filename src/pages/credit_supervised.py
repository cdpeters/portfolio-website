"""Layout for the background page.

Displays an example project background using markdown.

Variables:
    markdown
    layout
"""
from pathlib import Path

from dash import dcc, html, register_page

from utils.constants import ICONS, IDS, PAGE_METADATA

# Extract page name from the module name.
page = __name__.replace("pages.", "")
register_page(__name__, **PAGE_METADATA[page], id_page_link=IDS[f"page_{page}"]["link"])

pages_markdown_dir = Path(__file__).parents[1].joinpath("pages_markdown")

# Read the markdown file associated with this page in as string.
with open(pages_markdown_dir / f"{page}.md", "r", encoding="utf-8") as f:
    markdown_contents = f.read()

if PAGE_METADATA[page]["website"] is None:
    website = "N/A"
else:
    website = PAGE_METADATA[page]["website"]

metadata = html.Div(
    [
        #
        html.Div(
            [
                html.Div("Project Summary", className="font-semibold text-emerald-50"),
                dcc.Link(
                    [
                        html.Img(src=ICONS["github"], className="aspect-square h-5"),
                        html.Span("Source", className="align-middle text-emerald-50"),
                    ],
                    href=PAGE_METADATA[page]["repo"],
                    refresh=True,
                    target="_blank",
                    className="not-prose flex items-center justify-between gap-2",
                ),
            ],
            className="px-2 py-0.5 flex items-center justify-between bg-slate-700 rounded",
        ),
        html.Div(
            [
                #
                html.Div(
                    "Languages",
                    className="px-2 font-semibold col-start-1 col-span-1 row-start-1 row-span-1 text-slate-600",
                ),
                html.Div(
                    PAGE_METADATA[page]["languages"],
                    className="col-start-2 col-span-1 row-start-1 row-span-1",
                ),
                #
                html.Div(
                    "Libraries/Tools",
                    className="px-2 font-semibold col-start-1 col-span-1 row-start-2 row-span-1 text-slate-600",
                ),
                html.Div(
                    PAGE_METADATA[page]["libraries_tools"],
                    className="col-start-2 col-span-1 row-start-2 row-span-1",
                ),
                #
                html.Div(
                    "Concepts",
                    className="px-2 font-semibold col-start-1 col-span-1 row-start-3 row-span-1 text-slate-600",
                ),
                html.Div(
                    PAGE_METADATA[page]["concepts"],
                    className="col-start-2 col-span-1 row-start-3 row-span-1",
                ),
                #
                html.Div(
                    "Website",
                    className="px-2 font-semibold col-start-1 col-span-1 row-start-4 row-span-1 text-slate-600",
                ),
                html.Div(
                    website, className="col-start-2 col-span-1 row-start-4 row-span-1"
                ),
            ],
            className="py-1 grid grid-cols-[9rem_1fr] grid-row-4",
        ),
    ],
    className="",
)

markdown = dcc.Markdown(
    markdown_contents,
    link_target="_blank",
    dangerously_allow_html=True,
)

layout = html.Div(
    html.Div(
        [
            metadata,
            html.Hr(className="not-prose mx-2 mt-2 mb-10 border-slate-400"),
            markdown,
        ],
        className="prose prose-slate hover:prose-a:text-slate-500 max-w-3xl px-4 pb-10 pt-6 max-xs:prose-sm sm:prose-lg xl:prose-xl marker:text-slate-500 prose-headings:text-slate-700 prose-img:border prose-img:border-slate-700 prose-img:shadow-md prose-img:shadow-slate-600 max-xs:max-w-[100%] sm:px-7 md:px-8 xl:max-w-4xl",
    ),
    className="flex flex-wrap justify-center h-[calc(100vh-1.75rem)]",
)
