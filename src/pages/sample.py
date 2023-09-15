"""Layout for the background page.

Displays an example project background using markdown.

Variables:
    markdown
    layout
"""
from pathlib import Path

from dash import dcc, html, register_page

from utils.constants import IDS, PAGE_METADATA

# Extract page name from the module name.
page = __name__.replace("pages.", "")
register_page(__name__, **PAGE_METADATA[page], id_page_link=IDS[f"page_{page}"]["link"])

pages_markdown_dir = Path(__file__).parents[1].joinpath("pages_markdown")

# Read the markdown file associated with this page in as string.
with open(pages_markdown_dir / f"{page}.md", "r", encoding="utf-8") as f:
    markdown_contents = f.read()

markdown = dcc.Markdown(
    markdown_contents,
    dangerously_allow_html=True,
)

layout = html.Div(
    [
        html.Div(
            [
                html.P(
                    """This app will serve as a testing ground for dashboard
                    development. The intention is to use it as boilerplate for creating
                    dashboards in future projects."""
                ),
                markdown,
            ],
            className="prose prose-slate max-w-3xl px-4 pb-10 pt-6 sm:prose-lg xl:prose-xl prose-headings:text-slate-700 sm:px-7 md:px-8 xl:max-w-4xl",
        ),
    ],
    className="flex items-center flex-col h-[calc(100vh-1.75rem)]",
)
