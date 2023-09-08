"""Build a footer component with a link to the app source code on github.

Variables:
    footer_component
"""

from dash import dcc, html

from utils.constants import APP_SOURCE_CODE_URL, ICONS

footer_component = html.Div(
    dcc.Link(
        [
            html.Img(src=ICONS["github"], className="aspect-square h-3"),
            html.Div("Portfolio Source", className="text-emerald-50 text-[0.625rem]"),
        ],
        href=APP_SOURCE_CODE_URL,
        refresh=True,
        target="_blank",
        className="pr-1.5 py-1 flex space-x-1.5 items-center float-right",
    ),
    className="fixed left-0 bottom-0 right-0 z-40 bg-slate-700",
)
