"""Layout for the dashboard page.

Arranges different dashboard elements on the dashboard page.

Variables:
    bar_chart_row
    hawaii_line_chart_row
    table_row
    layout
"""

from dash import html, register_page

from components.figures import avg_precip_line_chart, avg_temp_line_chart, bar_chart
from components.table import hawaii_climate_table
from utils.constants import IDS

# Needed for the app to see this module as a page. The `navbar` argument is included so
# that this page will be added as a page link in the navbar.
register_page(
    __name__,
    sidebar=True,
    order=3,
    name="Dashboard",
    language="javascript",
    id_link=IDS[__name__.replace("pages.", "")]["link"],
)

dashboard_grid = html.Div(
    [
        html.Div(
            avg_temp_line_chart,
            className="w-[512px] shadow-md lg:justify-self-end lg:max-xl:w-[420px]",
        ),
        html.Div(
            bar_chart,
            className="w-[512px] shadow-md lg:justify-self-start lg:max-xl:w-[420px]",
        ),
        html.Div(
            avg_precip_line_chart,
            className="w-[512px] lg:justify-self-end shadow-md lg:max-xl:w-[420px]",
        ),
        html.Div(
            hawaii_climate_table,
            className="""z-0 shadow-md w-[512px] lg:justify-self-start
            lg:max-xl:w-[420px]""",
        ),
    ],
    className="grid gap-4 lg:grid-cols-2 max-lg:justify-items-center",
)

# `layout` is required for Dash multi-page apps.
layout = html.Div(
    [
        html.Div(
            [
                html.P(
                    "This is the Dash Test App dashboard.",
                    className="mb-4 text-inherit",
                ),
                dashboard_grid,
            ],
            className="p-4 text-slate-700 mb-8",
        ),
    ],
    className="min-h-screen",
)
