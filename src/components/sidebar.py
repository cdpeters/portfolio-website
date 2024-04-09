"""Build a sidebar component with page links.

The `create_sidebar` function uses `page_registry` and builds page links in sections
based on the primary language of the project. The callback `update_sidebar_style`
updates the styling of the page links when the link is active.

Functions:
    create_sidebar

Callbacks:
    update_sidebar_style
    toggle_page_link_visibility
"""
import re

import pandas as pd
from dash import Input, Output, State, callback, ctx, dcc, html, page_registry

from utils.constants import COLORS, ICONS, IDS, PAGE_METADATA, SECTIONS


def create_sidebar() -> html.Div:
    """Create the sidebar component with page links for navigation.

    `page_registry` page data is used to construct the sidebar's page links. A page is
    included if its metadata has a `sidebar` key with a value of `True` set when the
    page was registered.

    Returns
    -------
    html.Div
        A sidebar with language sections and a link to each page.

    Notes
    -----
    `create_sidebar` is a function (as opposed to simple named variable) in order to use
    `page_registry` within it. See the Dash documentation.
    """
    pages: list[dict] = [
        page for page in page_registry.values() if not page.get("sidebar_exclude")
    ]
    # Build the language sections as a dictionary of the form:
    # language_sections = {
    #     `language`: {
    #         "heading": `heading`,
    #         "links": [`link`, ...],
    #     }
    # }
    # This allows for easy assembly of the `sections` list below.
    language_sections = dict()
    # Any non project links will be collected in `non_project_links` and will not have a
    # section heading.
    non_project_links = list()
    for page in pages:
        language = page["section"]
        if language:
            # Assign a label for each language section.
            if language == "sql" or language == "cli":
                language_label = language.upper()
            elif language == "javascript":
                language_label = "JavaScript"
            else:
                language_label = language.title()
            language_heading = html.Span(
                language_label,
                className="text-left text-lg italic text-slate-500",
            )
            # The full heading (containing the language heading and the arrow icon) is
            # turned into a button which is easier to click on mobile.
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
        # Page links.
        link = dcc.Link(
            page["name"],
            id=page["id_page_link"],
            href=page["relative_path"],
            className="mx-2 mb-1 rounded-md py-[3px] pl-2 pr-2 text-left text-lg font-semibold text-emerald-50 duration-150 hover:bg-slate-700 hover:pl-3 hover:pr-1.5",
        )

        # Create the language key and its starting value if it does not exist yet. The
        # "links" key is an empty list because `link` is added in the `if` statement
        # that follows.
        if language and (language not in language_sections):
            language_sections[language] = {"heading": heading, "links": list()}

        if language:
            language_sections[language]["links"].append(link)
        else:
            non_project_links.append(link)

    # Each element of `sections` is a "section div" representing a language section. All
    # of the html for a given language section is contained within its corresponding
    # "section div".
    link_div = html.Div(non_project_links, className="flex flex-col")
    section_div = html.Div(link_div, className="mt-3")

    sections = [section_div]

    for language, section_data in language_sections.items():
        # `link_div` contains all page links for projects belonging to the `language`
        # section.
        link_div = html.Div(
            section_data["links"],
            className="flex flex-col",
        )
        # `link_div_wrapper` is used to allow for adding the class `hidden` via callback
        # which cannot be added to the previous `link_div` element since it is already
        # using a display property (display: flex;).
        link_div_wrapper = html.Div(link_div, id=IDS[f"section_{language}"]["link_div"])
        hr = html.Hr(className="mx-2 border-slate-700")
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
        className="""overflow-auto bg-slate-800 pb-6 transition-transform duration-300
        max-md:fixed max-md:bottom-0 max-md:left-0 max-md:top-[4rem] max-md:w-[15.25rem] max-md:-translate-x-full
        md:col-span-1 md:col-start-1 md:row-span-2 md:row-start-2""",
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
        "page_link_class": {
            page: State(
                component_id=IDS[f"page_{page}"]["link"],
                component_property="className",
            )
            for page in PAGE_METADATA
        },
    },
)
def update_sidebar_style(
    pathname: str, page_link_class: dict[str, str]
) -> dict[str, str]:
    """Update page link colors when a new link is active.

    Parameters
    ----------
    pathname : str
        Current path of the app.
    page_link_class : dict[str, str]
        The `className` property for each page link.

    Returns
    -------
    dict[str, str]
        The updated page link classes.
    """
    link_class = page_link_class.copy()

    inactive_text = COLORS["text_color_light"]
    inactive_hover = COLORS["hover_color_dark"]

    active_background = COLORS["bg_color_light"]
    active_text = COLORS["text_color_dark"]

    # Check if there was a link that was active and filter out all non-active links.
    lc = pd.Series(link_class)
    pattern_active = rf"(?<!\S){COLORS['bg_color_light']} ?"
    is_active = lc[lc.str.contains(pattern_active)]

    # Reset previously active page link to styling for inactive state.
    if not is_active.empty:
        previous_page = is_active.index[0]
        link_class[previous_page] = link_class[previous_page].replace(
            active_text, inactive_text
        )
        link_class[previous_page] = link_class[previous_page].replace(
            active_background, inactive_hover
        )

    # Remove the `/` from `pathname` in order to use it as an accessor in
    # `link_class`.
    if pathname == "/":
        page = "about_me"
    else:
        page = pathname.replace("/", "")
        page = page.replace("-", "_")

    # Change the link associated with the new path to the active state.
    try:
        link_class[page] = link_class[page].replace(inactive_text, active_text)
        link_class[page] = link_class[page].replace(inactive_hover, active_background)
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
def toggle_page_link_visibility(
    section_button_clicks: dict[str, int],
    section_icon_class: dict[str, str],
    link_div_class: dict[str, str],
) -> dict[str, dict[str, str]]:
    """Show or hide page links in a given section on click.

    The default state is all page links are showing.

    Parameters
    ----------
    section_button_clicks : dict[str, int]
        The `n_click` property for each section button.
    section_icon_class : dict[str, str]
        The `className` property for each section arrow icon.
    link_div_class : dict[str, str]
        The `className` property for each `link_div_wrapper` containing the page links.

    Returns
    -------
    dict[str, dict[str, str]]
        Updated `section_icon_class` and `link_div_class` properties.
    """
    triggered_id = ctx.triggered_id.replace("_button", "")

    rotate = "-rotate-90"
    hide = "hidden"
    show = ""

    pattern = rf"^{rotate} "
    rotate_match = re.search(pattern, section_icon_class[triggered_id])

    # `rotate_match` is True when the arrow icon is pointing sideways (i.e. links are
    # hidden).
    if rotate_match:
        section_icon_class[triggered_id] = section_icon_class[triggered_id].replace(
            rotate_match[0], ""
        )

        link_div_class[triggered_id] = show
    else:
        section_icon_class[
            triggered_id
        ] = f"{rotate} {section_icon_class[triggered_id]}"

        link_div_class[triggered_id] = hide

    return {
        "section_icon_class": section_icon_class,
        "link_div_class": link_div_class,
    }
