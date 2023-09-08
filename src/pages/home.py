"""Layout for the home page.

Variables:
    layout
"""

from dash import html, register_page

from utils.constants import IDS

# Needed for the app to see this module as a page.
register_page(
    __name__,
    path="/",
    sidebar=True,
    order=0,
    name="Home",
    language="home",
    id_link=IDS[__name__.replace("pages.", "")]["link"],
)

layout = html.Div(
    html.Div(
        "Welcome to the Dash Test App",
        className="pb-32 font-semibold text-center text-2xl md:text-4xl lg:text-5xl xl:text-6xl text-slate-700",
    ),
    className="flex items-center justify-center h-screen",
)
