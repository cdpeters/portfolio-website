"""Layout for the home page.

Variables:
    layout
"""

from dash import html, register_page

from utils.constants import IDS, PAGE_METADATA

page = __name__.replace("pages.", "")
# Needed for the app to see this module as a page.
register_page(
    __name__, path="/", **PAGE_METADATA[page], id_page_link=IDS[f"page_{page}"]["link"]
)

layout = html.Div(
    html.Div(
        "Welcome to the Dash Test App",
        className="text-center text-2xl font-semibold text-slate-700 md:text-4xl lg:text-5xl xl:text-6xl",
    ),
    className="flex h-[calc(100vh-2.5rem-1.5rem)] flex-col items-center justify-center md:h-[calc(100vh-1.5rem)]",
)
