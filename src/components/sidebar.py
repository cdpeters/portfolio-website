"""Build a sidebar component with page links.

The `create_sidebar` function takes in the page registry and builds page links
in sections based on the primary language of the project. There is also a header that
redirects to the home page of the app. The callback `update_sidebar_style` updates the
styling of the page links when the link is active.

Functions:
    create_sidebar

Callbacks:
    update_sidebar_style
    toggle_page_links_visibility
"""
import re

import pandas as pd
from dash import Input, Output, State, callback, ctx, dcc, html, page_registry

from utils.constants import COLORS, ICONS, IDS, PAGE_METADATA, SECTIONS
from utils.funcs import update_utility_classes


def create_sidebar() -> html.Div:
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
    `create_sidebar` is a function (as opposed to simple named variable) in
    order to use `page_registry` within it. See the documentation for Plotly Dash.
    """
    pages = [page for page in page_registry.values() if page.get("sidebar")]
    # Build the sections based on language as a dictionary of the form:
    # {
    #     `language`: {
    #         "heading": `section_heading`,
    #         "links": [`link`, ...],
    #     }
    # }
    # This allows for easy assembly of the `sections` list below.
    language_sections = dict()
    non_language_links = list()
    for page in pages:
        # Only include pages that are meant to be shown in the sidebar.
        language = page["section"]
        if language:
            if language == "sql" or language == "cli":
                language_title = language.upper()
            elif language == "javascript":
                language_title = "JavaScript"
            else:
                language_title = language.title()
            language_heading = html.Span(
                language_title,
                className="text-left italic text-lg text-slate-500",
            )
            heading = html.Button(
                [
                    language_heading,
                    html.Img(
                        id=IDS[f"section_{language}"]["icon"],
                        src=ICONS["section_arrow"],
                        className="aspect-square h-3.5 transition-transform",
                    ),
                ],
                id=IDS[f"section_{language}"]["button"],
                className="flex items-center justify-between px-2.5 pb-2.5 pt-3.5",
                type="button",
            )

        link = dcc.Link(
            page["name"],
            id=page["id_page_link"],
            href=page["relative_path"],
            className="py-1 pl-6 pr-2 text-left font-semibold text-emerald-50 transition-transform hover:bg-slate-700 hover:pl-7 hover:pr-1.5 text-xl sm:text-lg",
        )

        # Create the language key and its starting value if it does not exist yet.
        if language and (language not in language_sections):
            language_sections[language] = {"heading": heading, "links": list()}

        if language:
            language_sections[language]["links"].append(link)
        else:
            non_language_links.append(link)

    # Each element of `sections` is a "section div" representing an individual language
    # section. All of the html for a given language section is contained within its
    # corresponding "section div".
    link_div = html.Div(non_language_links, className="flex flex-col")
    section_div = html.Div(link_div, className="mt-3")
    hr = html.Hr(className="max-md:hidden md:border-slate-700")

    sections = [hr, section_div]

    for language, section_data in language_sections.items():
        # `link_div` contains all page links for projects belonging to the `language`
        # section.
        hr = html.Hr(className="mx-2 border-slate-700")
        link_div = html.Div(
            section_data["links"],
            className="flex flex-col",
        )
        link_div_wrapper = html.Div(
            link_div, id=IDS[f"section_{language}"]["link_div"], className=""
        )

        section_div = html.Div(
            [hr, section_data["heading"], link_div_wrapper],
            className="mt-3 flex flex-col",
        )

        sections.append(section_div)

    return html.Div(
        # `page_links` has to be unpacked since it is a list (i.e. the `children`
        # argument can be a list but it must not contain a list as an element).
        sections,
        id=IDS["sidebar"],
        className="overflow-auto bg-slate-800 transition-transform duration-300 max-md:fixed max-md:bottom-0 max-md:left-0 max-md:-translate-x-full max-sm:top-[4rem] max-sm:w-[13rem] sm:max-md:top-[3rem] sm:max-md:w-[12rem] md:col-span-1 md:col-start-1 md:row-span-2 md:row-start-2",
    )


@callback(
    output={
        page: Output(
            component_id=IDS[f"page_{page}"]["link"], component_property="className"
        )
        for page in PAGE_METADATA
    },
    inputs={
        "pathname": Input(component_id=IDS["location"], component_property="pathname"),
        "input_link_class": {
            page: State(
                component_id=IDS[f"page_{page}"]["link"],
                component_property="className",
            )
            for page in PAGE_METADATA
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
    if not is_active.empty:
        previous_page = str(is_active.index[0])
        # assert previous_page is not None
        link_class[previous_page] = update_utility_classes(
            current_classes=is_active.loc[previous_page],
            remove_classes=[COLORS["bg_color_light"], COLORS["text_color_dark"]],
            add_classes=[COLORS["text_color_light"], COLORS["hover_color_dark"]],
            ignore_prefix_warning=True,
        )

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
            remove_classes=[COLORS["text_color_light"], COLORS["hover_color_dark"]],
            add_classes=[COLORS["bg_color_light"], COLORS["text_color_dark"]],
            ignore_prefix_warning=True,
        )
    except KeyError:
        print(f"The page route '{page}' does not exist.")

    return link_class


@callback(
    output={
        "section_icon_class": {
            f"section_{language}": Output(
                component_id=IDS[f"section_{language}"]["icon"],
                component_property="className",
            )
            for language in SECTIONS
        },
        "link_div_class": {
            f"section_{language}": Output(
                component_id=IDS[f"section_{language}"]["link_div"],
                component_property="className",
            )
            for language in SECTIONS
        },
    },
    inputs={
        "section_button_clicks": {
            f"section_{language}": Input(
                component_id=IDS[f"section_{language}"]["button"],
                component_property="n_clicks",
            )
            for language in SECTIONS
        },
        "section_icon_class": {
            f"section_{language}": State(
                component_id=IDS[f"section_{language}"]["icon"],
                component_property="className",
            )
            for language in SECTIONS
        },
        "link_div_class": {
            f"section_{language}": State(
                component_id=IDS[f"section_{language}"]["link_div"],
                component_property="className",
            )
            for language in SECTIONS
        },
    },
    prevent_initial_call=True,
)
def toggle_page_links_visibility(
    section_button_clicks: dict[str, int],
    section_icon_class: dict[str, str],
    link_div_class: dict[str, str],
) -> dict[str, dict[str, str]]:
    """Show or hide page links per section on click.

    Parameters
    ----------
    section_button_clicks : dict[str, int]
        The `n_click` property for each section button.
    section_icon_class : dict[str, str]
        The `className` property for each section arrow icon.
    link_div_class : dict[str, str]
        The `className` property for each div containing the page links.

    Returns
    -------
    dict[str, dict[str, str]]
        Updated `section_icon_class` and `link_div_class` properties.
    """
    triggered_id = ctx.triggered_id.replace("_button", "")

    rotate = "-rotate-90"
    translate_in = "hidden"
    translate_out = ""

    pattern = rf"(?<!\S){rotate} ?"
    rotate_match = re.search(pattern, section_icon_class[triggered_id])

    if rotate_match:
        section_icon_class[triggered_id] = section_icon_class[triggered_id].replace(
            rotate_match[0], ""
        )
        link_div_class[triggered_id] = link_div_class[triggered_id].replace(
            translate_in, translate_out
        )
    else:
        section_icon_class[
            triggered_id
        ] = f"{rotate} {section_icon_class[triggered_id]}"
        link_div_class[triggered_id] = link_div_class[triggered_id].replace(
            translate_out, translate_in
        )

    return {
        "section_icon_class": section_icon_class,
        "link_div_class": link_div_class,
    }
