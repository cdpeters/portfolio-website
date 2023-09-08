"""Build a sidebar component with page links.

The `create_sidebar_component` function takes in the page registry and builds page links
in sections based on the primary language of the project. There is also a header that
redirects to the home page of the app. The callback `update_sidebar_style` updates the
styling of the page links when the link is active.

Functions:
    create_sidebar_component

Callbacks:
    update_sidebar_style
"""
import pandas as pd
from dash import Input, Output, State, callback, dcc, html, page_registry

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
    `create_sidebar_component` is a function (as opposed to simple named variable) in
    order to use `page_registry` within it. See the documentation for Plotly Dash.
    """
    site_heading = html.Div(
        [
            dcc.Link(
                "Project Portfolio",
                href="/",
            ),
        ],
        className="py-2.5 px-2 text-center text-sm font-bold bg-slate-900 text-emerald-50",
    )

    # Build the sections based on language as a dictionary of the form:
    # {
    #     `language`: {
    #         "heading": `language_heading`,
    #         "links": [`link`, ...],
    #     }
    # }
    # This allows for easy assembly of the `sections` list below.
    language_sections = {}
    for page in page_registry.values():
        # Only include pages that are meant to be shown in the sidebar.
        if page.get("sidebar"):
            language = page["language"]
            language_title = language.title() if language != "sql" else language.upper()
            language_heading = html.Div(
                language_title,
                className="px-1.5 pt-2 pb-1 italic text-left text-slate-600 text-xs font-semibold",
            )

            link = dcc.Link(
                page["name"],
                id=page["id_link"],
                href=page["relative_path"],
                className="pl-4 pr-2 py-1.5 font-semibold text-sm text-left text-emerald-50 hover:bg-slate-700 hover:pl-[1.12rem] hover:pr-1.5 transition-all",
            )

            # Create the language key and its starting value if it does not exist yet.
            if language not in language_sections:
                language_sections[language] = {"heading": language_heading, "links": []}
            language_sections[language]["links"].append(link)

    # Each element of `sections` is a "section div" representing an individual language
    # section. All of the html for a given language section is contained within its
    # corresponding "section div".
    sections = []
    for language, section_data in language_sections.items():
        # `link_div` contains all page links for projects belonging to the `language`
        # section.
        link_div = html.Div(section_data["links"], className="flex flex-col")

        section_div_class_name = "mt-3"
        # Exclude a heading for the home page link (a stylistic choice).
        if language == "home":
            section_div = html.Div(link_div, className=section_div_class_name)
        else:
            section_div = html.Div(
                [section_data["heading"], link_div], className=section_div_class_name
            )
        sections.append(section_div)

    return html.Div(
        # `page_links` has to be unpacked since it is a list (i.e. the `children`
        # argument can be a list but it must not contain a list as an element).
        [
            # Location needed to collect the current path for the styling callback.
            dcc.Location(id=IDS["location"], refresh=False),
            site_heading,
            *sections,
        ],
        className="hidden md:block fixed top-0 left-0 z-50 h-screen md:w-36 bg-slate-800 overflow-auto",
    )


@callback(
    output={
        page: Output(component_id=IDS[page]["link"], component_property="className")
        for page in SIDEBAR_PAGE_NAMES
    },
    inputs={
        "pathname": Input(component_id=IDS["location"], component_property="pathname"),
        "input_link_class": {
            page: State(component_id=IDS[page]["link"], component_property="className")
            for page in SIDEBAR_PAGE_NAMES
        },
    },
)
def update_sidebar_style(
    pathname: str, input_link_class: dict[str, str]
) -> dict[str, str]:
    """Update link colors when a link is active.

    Parameters
    ----------
    pathname : str
        Current pathname of the app.
    input_link_class : dict[str, str]
        Contains the class attribute for each page link.

    Returns
    -------
    dict[str, str]
        Contains the updated page link classes.
    """
    link_class = input_link_class.copy()

    # Reset previously active page link to styling for inactive state ------------------
    iis = pd.Series(link_class)
    pattern_active = COLORS["bg_color_light"]
    is_active = iis[iis.str.contains(pattern_active)]

    # If there is a previously active page then its classes will be updated to make it
    # inactive.
    previous_pathname: str | None
    if not is_active.empty:
        previous_pathname = str(is_active.index[0])
        assert previous_pathname is not None
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
        page = page.replace("-", "_")

    # Try/except is used because it is possible to enter a route that doesn't exist,
    # resulting in a KeyError when trying to access that `page` name.
    try:
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

    return link_class
