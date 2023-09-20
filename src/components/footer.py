"""Build a footer component with a link to the portfolio source code on github.

Variables:
    footer
"""

from dash import dcc, html

from utils.constants import APP_SOURCE_CODE_URL, ICONS

footer = html.Div(
    dcc.Link(
        [
            html.Img(src=ICONS["github"], className="aspect-square h-5"),
            html.Span("Portfolio Source", className="align-middle text-emerald-50"),
        ],
        href=APP_SOURCE_CODE_URL,
        refresh=True,
        target="_blank",
        className="flex items-center justify-end gap-2 pr-2.5",
    ),
    className="col-span-2 col-start-1 row-span-1 row-start-3 flex items-center justify-end bg-slate-700 md:col-span-1 md:col-start-2 md:row-span-1 md:row-start-3",
)
