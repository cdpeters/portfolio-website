"""Layout for the home page.

Variables:
    layout
"""

from dash import html, register_page

from utils.constants import ICONS, IDS

# Needed for the app to see this module as a page.
register_page(
    __name__,
    path="/",
    sidebar=True,
    order=0,
    id_icon=IDS["home"]["icon"],
    id_link=IDS["home"]["link"],
    icon_light=ICONS["home"]["light"],
    icon_dark=ICONS["home"]["dark"],
)

layout = html.Div(
    html.Div(
        "Welcome to the Dash Test App",
        className="text-5xl pb-40 text-slate-700 xl:text-6xl",
    ),
    className="flex items-center justify-center h-screen",
)
