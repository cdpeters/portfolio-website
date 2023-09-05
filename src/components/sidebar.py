"""Build a sidebar component with page links.

The `create_sidebar_component` function takes in the page registry and builds page
links. There is also a header that redirects to the home page of the app. The callback
`update_sidebar_style` updates the styling of the page links when the link is active.

Functions:
    create_sidebar_component

Callbacks:
    update_sidebar_style
"""
import re

import pandas as pd
from dash import Input, Output, State, callback, dcc, html, page_registry
from rich import print

from utils.constants import COLORS, IDS, SIDEBAR_PAGE_NAMES
from utils.funcs import update_utility_classes


def create_sidebar_component() -> html.Div:
    """Create the sidebar component with page links for navigation.

    `page_registry` page data is used to construct the sidebar's page links. A page is
    included if it has a `sidebar` key with a value of True set when the page was
    registered.

    Returns
    -------
    html.Div
        A sidebar with a link to each page.

    Notes
    -----
    `create_sidebar_component` is a function in order to use `page_registry` within it.
    See the documentation for Plotly Dash.
    """
    heading = dcc.Link(
        [
            html.Div(
                "Code Portfolio",
                className="py-1.5 text-center font-semibold text-emerald-50",
            ),
        ],
        href="/",
    )

    # `page_links` is a list comprehension.
    page_links = [
        dcc.Link(
            [
                # Page icon.
                html.Img(
                    id=page["id_icon"],
                    src=page["icon_light"],
                    className="aspect-square w-3",
                ),
                # Page name.
                html.Div(
                    page["name"],
                    className="text-inherit bg-inherit break-words",
                ),
            ],
            id=page["id_link"],
            href=page["relative_path"],
            className="px-2 py-2 flex space-x-2 items-center text-xs text-emerald-50 hover:bg-slate-700 hover:px-2.5 transition-all",
        )
        for page in page_registry.values()
        if page.get("sidebar")
    ]

    return html.Div(
        # `page_links` has to be unpacked since it is a list (i.e. the `children`
        # argument can be a list but it must not contain a list as an element).
        [
            # Location needed to collect the current path for the styling callback.
            dcc.Location(id=IDS["location"], refresh=False),
            heading,
            *page_links,
        ],
        className="fixed top-0 left-0 h-screen w-32 bg-slate-800 overflow-auto",
    )


@callback(
    output={
        "output_icon_src": {
            page: Output(component_id=IDS[page]["icon"], component_property="src")
            for page in SIDEBAR_PAGE_NAMES
        },
        "output_link_class": {
            page: Output(component_id=IDS[page]["link"], component_property="className")
            for page in SIDEBAR_PAGE_NAMES
        },
    },
    inputs={
        "pathname": Input(component_id=IDS["location"], component_property="pathname"),
        "input_icon_src": {
            page: State(component_id=IDS[page]["icon"], component_property="src")
            for page in SIDEBAR_PAGE_NAMES
        },
        "input_link_class": {
            page: State(component_id=IDS[page]["link"], component_property="className")
            for page in SIDEBAR_PAGE_NAMES
        },
    },
)
def update_sidebar_style(pathname, input_icon_src, input_link_class):
    """Update icons and link colors when a link is active.

    Parameters
    ----------
    pathname : str
        Current pathname of the app.
    input_icon_src : dict[str, str]
        Contains the src attribute for each page link's icon.
    input_link_class : dict[str, str]
        Contains the class attribute for each page link.

    Returns
    -------
    dict[str, dict[str, str]]
        Contains the updated icon src attributes and page link class attributes.
    """
    icon_src = input_icon_src.copy()
    link_class = input_link_class.copy()

    # Reset previously active page link to styling for inactive state ------------------
    iis = pd.Series(link_class)
    pattern_active = COLORS["bg_color_light"]
    is_active = iis[iis.str.contains(pattern_active)]

    # If there is a page with a dark icon, change it back to light icon.
    if not is_active.empty:
        previous_pathname = is_active.index[0]
        icon_src[previous_pathname] = re.sub(
            r"_dark\.", "_light.", icon_src[previous_pathname]
        )
        link_class[previous_pathname] = update_utility_classes(
            current_classes=is_active.loc[previous_pathname],
            remove_classes=[COLORS["bg_color_light"], COLORS["text_color_dark"]],
            add_classes=[
                COLORS["text_color_light"],
                COLORS["hover_color_dark"],
            ],
            ignore_prefix_warning=True,
        )
    else:
        previous_pathname = None

    # Update current active page link to styling for active state ----------------------
    if pathname == "/":
        page = "home"
    else:
        page = pathname.replace("/", "")

    # Try/except is used because it is possible to enter a route that doesn't exist,
    # resulting in a KeyError when trying to access that `page` name.
    try:
        icon_src[page] = re.sub(r"_light\.", "_dark.", icon_src[page])
        link_class[page] = update_utility_classes(
            current_classes=link_class[page],
            remove_classes=[
                COLORS["text_color_light"],
                COLORS["hover_color_dark"],
            ],
            add_classes=[COLORS["bg_color_light"], COLORS["text_color_dark"]],
            ignore_prefix_warning=True,
        )
    except KeyError:
        print(f"The page route '{page}' does not exist.")

    return {
        "output_icon_src": {**icon_src},
        "output_link_class": {**link_class},
    }
