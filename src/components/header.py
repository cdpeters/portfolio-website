"""Build a header component with a navigation menu button for small screens.

A header component is created with a contact information section and a navigation
button that allows access to the sidebar on smaller screens.

Variables:
    header

Callbacks:
    show_sidebar
"""
import re

from dash import Input, Output, State, callback, ctx, dcc, html

from utils.constants import ICONS, IDS

# Navigation button containing the nav menu icon.
nav_button = html.Button(
    html.Img(
        id=IDS["header_nav"]["icon"],
        src=ICONS["nav"],
        title="Navigation Menu",
        className="aspect-square h-7 transition-transform duration-300",
    ),
    id=IDS["header_nav"]["button"],
    className="py-2 md:hidden",
    type="button",
)

# Contact info and avatar.
contact_info = dcc.Link(
    "Project Portfolio",
    href="/",
    className="text-center text-xl text-slate-50",
)

header = html.Div(
    [nav_button, contact_info],
    className="""col-span-2 col-start-1 row-span-1 row-start-1
    flex items-center justify-between border-b-[1px] border-slate-700 bg-slate-900 px-4
    md:col-span-1 md:col-start-1 md:row-span-1 md:row-start-1 md:justify-center""",
)


@callback(
    output={
        "nav_icon_class": Output(
            component_id=IDS["header_nav"]["icon"], component_property="className"
        ),
        "sidebar_class": Output(
            component_id=IDS["sidebar"], component_property="className"
        ),
    },
    inputs={
        "clicks": Input(
            component_id=IDS["header_nav"]["button"], component_property="n_clicks"
        ),
        "pathname": Input(component_id=IDS["location"], component_property="pathname"),
        "nav_icon_class": State(
            component_id=IDS["header_nav"]["icon"], component_property="className"
        ),
        "sidebar_class": State(
            component_id=IDS["sidebar"], component_property="className"
        ),
    },
)
def show_sidebar(
    clicks: int, pathname: str, nav_icon_class: str, sidebar_class: str
) -> dict[str, str]:
    """Show sidebar on click of the nav button.

    Parameters
    ----------
    clicks : int
        The `n_clicks` property for the nav button.
    pathname : str
        The current path of the website.
    nav_icon_class : str
        The `className` property for the nav icon.
    sidebar_class : str
        The `className` property for the sidebar.

    Returns
    -------
    dict[str, str]
        The updated `className` properties for the nav icon and sidebar.
    """
    rotate = "-rotate-90"
    show = "max-md:translate-none"
    hide = "max-md:-translate-x-full"
    animate = "max-md:animate-ping-not-infinite"

    # Check if `animate` is already in `nav_icon_class`.
    pattern_animate = rf"^{animate} "
    animate_match = re.search(pattern_animate, nav_icon_class)

    # Check if `rotate` is already in `nav_icon_class`.
    pattern_rotate = rf"^{rotate} "
    rotate_match = re.search(pattern_rotate, nav_icon_class)

    # Give the icon a "ping" animation when the app is initially loaded.
    if not clicks:
        nav_icon_class = f"{animate} {nav_icon_class}"
        return {
            "nav_icon_class": nav_icon_class,
            "sidebar_class": sidebar_class,
        }
    elif animate_match:
        nav_icon_class = nav_icon_class.replace(animate_match[0], "")

    triggered_id = ctx.triggered_id
    # If the sidebar is showing (the icon has been rotated) and the location component
    # triggered the callback, then the sidebar is hidden and icon rotated back.
    if rotate_match and triggered_id == IDS["location"]:
        # Remove the icon rotation and hide the sidebar.
        nav_icon_class = nav_icon_class.replace(rotate_match[0], "")
        sidebar_class = sidebar_class.replace(show, hide)
    # If the nav button triggered the callback then we check if the icon had been
    # rotated in order to know whether to show or hide the sidebar.
    elif triggered_id == IDS["header_nav"]["button"]:
        if rotate_match:
            # Remove the icon rotation and hide the sidebar.
            nav_icon_class = nav_icon_class.replace(rotate_match[0], "")
            sidebar_class = sidebar_class.replace(show, hide)
        else:
            # Add the icon rotation and show the sidebar.
            nav_icon_class = f"{rotate} {nav_icon_class}"
            sidebar_class = sidebar_class.replace(hide, show)

    return {
        "nav_icon_class": nav_icon_class,
        "sidebar_class": sidebar_class,
    }
