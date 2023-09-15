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
from utils.constants import IDS, PAGE_METADATA

page = __name__.replace("pages.", "")
register_page(__name__, **PAGE_METADATA[page], id_page_link=IDS[f"page_{page}"]["link"])

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
            className="w-[512px] shadow-md lg:justify-self-end lg:max-xl:w-[420px]",
        ),
        html.Div(
            hawaii_climate_table,
            className="z-0 w-[512px] shadow-md lg:justify-self-start lg:max-xl:w-[420px]",
        ),
    ],
    className="grid gap-4 max-lg:justify-items-center lg:grid-cols-2",
)

# `layout` is required for Dash multi-page apps.
layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    "This is the Dash Test App dashboard.",
                    className="mb-4 text-inherit font-semibold text-lg",
                ),
                dashboard_grid,
            ],
            className="p-4 text-slate-700",
        ),
    ],
    className="flex items-center flex-col gap-4 h-[calc(100vh-1.75rem)]",
)
