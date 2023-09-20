"""Layout for the home page.

Variables:
    layout
"""

from dash import html, register_page

from utils.constants import IDS, PAGE_METADATA

# Extract the page name from the module name.
page = __name__.replace("pages.", "")
page_metadata = PAGE_METADATA[page].copy()

# Registering page is needed for the app to see this module as a page.
register_page(
    __name__, path="/", **page_metadata, id_page_link=IDS[f"page_{page}"]["link"]
)

layout = html.Div(
    html.H1(
        "I Swear That Guitar is Blue",
        className="px-4 pb-12 text-center text-3xl font-bold text-slate-700 md:pb-16 md:text-4xl lg:text-5xl xl:text-6xl",
    ),
    className="flex h-[calc(100vh-4rem-2.5rem)] flex-col items-center justify-center md:h-[calc(100vh-1.75rem)]",
)
