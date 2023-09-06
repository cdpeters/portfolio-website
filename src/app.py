"""Overall app layout for a multi-page application.

Variables:
    app
"""

import dash
from dash import Dash, html

from components.footer import footer_component
from components.sidebar import create_sidebar_component

# Creates app, sets external stylesheets, and configures the app to be multi-page.
app = Dash(
    name=__name__,
    use_pages=True,
    title="Dash Test App",
    assets_ignore="input.css",
)

server = app.server

# Place the navbar and the container for page content within the app.
app.layout = html.Div(
    [
        create_sidebar_component(),
        # Main Content.
        html.Div(
            [
                # Location for page contents.
                dash.page_container,
                footer_component,
            ],
            className="md:ml-32 bg-gradient-to-br from-white to-slate-300 h-auto flex-grow",
        ),
    ],
    className="flex",
)

if __name__ == "__main__":
    app.run(debug=True)
