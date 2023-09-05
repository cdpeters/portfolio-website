"""Build a footer component with a link to the app source code on github.

Variables:
    footer_component
"""

from dash import dcc, html

from utils.constants import APP_SOURCE_CODE_URL, ICONS

footer_component = html.Div(
    html.Div(
        dcc.Link(
            [
                html.Img(src=ICONS["github"], className="aspect-square h-3.5"),
                html.Div("Portfolio Source", className="text-emerald-50 text-xs"),
            ],
            href=APP_SOURCE_CODE_URL,
            refresh=True,
            target="_blank",
            className="px-3 py-1 flex space-x-1.5 items-center",
        ),
        className="flex items-center justify-between text-sm float-right",
    ),
    className="fixed left-32 bottom-0 right-0 z-40 bg-slate-700",
)
