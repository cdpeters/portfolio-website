"""Overall app layout for a multi-page application.

Variables:
    app
"""

import dash
from dash import Dash, dcc, html

from components.footer import footer
from components.header import header
from components.sidebar import create_sidebar
from utils.constants import IDS

# Creates app, sets external stylesheets, and configures the app to be multi-page.
app = Dash(
    name=__name__,
    use_pages=True,
    title="Portfolio",
    assets_ignore="input.css",
)

server = app.server

# Place the navbar and the container for page content within the app.
app.layout = html.Div(
    [
        # Used in callbacks to detect page route changes.
        dcc.Location(id=IDS["location"]),
        header,
        # Page Content.
        html.Div(
            dash.page_container,
            className="""col-span-2 col-start-1 row-span-1 row-start-2
            bg-gradient-to-br from-white from-30% via-slate-50 via-70% to-slate-300
            md:col-span-1 md:col-start-2 md:row-span-2 md:row-start-1""",
        ),
        create_sidebar(),
        footer,
    ],
    className="tap-color-transparent grid h-screen grid-cols-[15.25rem_1fr] grid-rows-[4rem_1fr_2.5rem] md:grid-rows-[5rem_1fr_1.75rem]",
)
