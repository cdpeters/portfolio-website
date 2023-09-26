"""Layout for the home page.

Variables:
    layout
"""

from dash import dcc, html, register_page

from utils.constants import EXTERNAL_LINKS, ICONS, IDS, IMAGES, PAGE_METADATA

# Extract the page name from the module name.
page = __name__.replace("pages.", "")
page_metadata = PAGE_METADATA[page].copy()

# Registering page is needed for the app to see this module as a page.
register_page(
    __name__, path="/", **page_metadata, id_page_link=IDS[f"page_{page}"]["link"]
)

professional_links = html.Div(
    [
        dcc.Link(
            html.Img(src=ICONS["email"], className="h-5 sm:h-6"),
            href=EXTERNAL_LINKS["email"],
            refresh=True,
            target="_blank",
            title="Email",
            className="",
        ),
        dcc.Link(
            html.Img(src=ICONS["resume"], className="h-5 sm:h-6"),
            href=EXTERNAL_LINKS["resume"],
            refresh=True,
            target="_blank",
            title="Resume",
            className="",
        ),
        dcc.Link(
            html.Img(src=ICONS["linkedin"], className="h-5 sm:h-6"),
            href=EXTERNAL_LINKS["linkedin"],
            refresh=True,
            target="_blank",
            title="LinkedIn",
            className="",
        ),
        dcc.Link(
            html.Img(src=ICONS["github_dark"], className="h-5 sm:h-6"),
            href=EXTERNAL_LINKS["github"],
            refresh=True,
            target="_blank",
            title="Github",
            className="",
        ),
    ],
    className="flex items-center justify-around text-slate-500 w-full",
)

face = html.Img(
    src=IMAGES["face"],
    className="not-prose aspect-square rounded-full border-8 border-slate-300 h-40 md:h-44 lg:h-56",
)

heading_group = html.Div(
    [
        html.H1("Hi, I'm Chris.", className=""),
        html.H4(
            "Thanks for stopping by!",
            className="pt-0.5 pb-1 rounded-md text-center bg-slate-200 w-full",
        ),
        professional_links,
    ],
    className="flex flex-col items-center max-xs:gap-8 xs:h-full xs:justify-around",
)

tagline = html.P(
    "I'm a data analyst with a passion for combining math and programming to solve puzzles and seek insight about the world.",
    className="max-xs:px-[5%] px-[7%] md:px-[7%] lg:px-[9%] max-xs:text-justify text-center italic font-semibold",
)

face_blurb = html.Div(
    [
        html.Div(
            [
                face,
                heading_group,
            ],
            className="flex max-xs:flex-col items-center justify-center max-xs:gap-6 xs:gap-6 sm:gap-7 lg:gap-8",
        ),
        tagline,
    ],
    className="flex flex-col items-center justify-center gap-8 xs:gap-3 text-slate-700 h-[calc(100vh-4rem-2.5rem-1.5rem-1.5rem)] md:h-[calc(100vh-1.75rem-1.5rem-1.5rem)]",
)


layout = html.Div(
    # Width and padding container.
    html.Div(
        face_blurb,
        className="""prose prose-slate max-w-full px-4 py-6
        sm:prose-lg lg:prose-xl 2xl:prose-2xl
        marker:text-slate-500 prose-headings:m-0
        prose-h1:text-4xl prose-h1:font-bold prose-h1:leading-tight prose-h1:text-slate-700
        prose-h4:text-slate-500
        prose-p:m-0 prose-p:text-slate-500 hover:prose-a:text-slate-500 prose-img:m-0
        max-xs:prose-h1:text-[2.625rem]
        xs:max-w-3xl
        xs:px-8
        sm:prose-h1:text-[2.625rem]
        md:prose-h1:text-5xl
        lg:prose-h1:text-6xl xl:max-w-4xl xl:prose-h1:text-7xl
        2xl:max-w-5xl backdrop-blur-[2px]""",
    ),
    className="bg-[url('/assets/images/math.png')] bg-center bg-cover xl:bg-bottom flex h-[calc(100vh-4rem-2.5rem)] flex-col items-center md:h-[calc(100vh-1.75rem)] overflow-auto",
)
