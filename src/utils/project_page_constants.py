"""Constants used in each project page.

The reason for this constants file is for maintainability of project pages. Each project
page file is now exactly the same (essentially a template) with all of the necessary
constants imported in.

In regards to the repeated use of the `className` variable below, this is done as a work
around due to the limitations of the tailwindcss intellisense VScode extension. This
extension only recognizes variables that are variants of the word "class". Additionally,
the extension does not work with python f-strings so common classes are not extracted
out and replaced by variables, they are instead left as is in the standard string
literal.

Constants:
    PAGE_SUMMARY_KEYS
    SUMMARY_BAR
    SUMMARY_DATA
    LAYOUT

"""
from typing import Any

from utils.constants import ICONS

# The keys for the data in the summary, repo is excluded since it is in the summary
# title bar.
SUMMARY_KEYS = ("languages", "libraries_tools", "concepts", "website")


# Summary title bar --------------------------------------------------------------------
SUMMARY_BAR: dict[str, Any] = dict()

className = "px-2 py-0.5 flex items-center justify-between bg-slate-700 rounded"
SUMMARY_BAR["class"] = className


# Summary title bar label.
className = "font-semibold text-emerald-50"
SUMMARY_BAR["div"] = {"label": "Project Summary", "class": className}


# Repo Link.
className = "not-prose flex items-center justify-center gap-2"
SUMMARY_BAR["link"] = {"class": className}

className = "aspect-square h-5 lg:h-6"
SUMMARY_BAR["img"] = {"src": ICONS["github_light"], "class": className}

className = "align-middle text-emerald-50"
SUMMARY_BAR["span"] = {"label": "Source", "class": className}


# Summary data -------------------------------------------------------------------------
SUMMARY_DATA: dict[str, Any] = dict()

className = "py-1 px-2 grid grid-cols-[8.5em_1fr] grid-row-4 gap-y-2"
SUMMARY_DATA["class"] = className


# Languages.
# Label div.
className = "font-semibold col-start-1 col-span-1 row-start-1 row-span-1 text-slate-700"
SUMMARY_DATA["languages"] = {"label_div": {"label": "Languages", "class": className}}
# Data div.
className = "col-start-2 col-span-1 row-start-1 row-span-1"
SUMMARY_DATA["languages"]["data_div"] = {"class": className}


# Libraries/Tools.
className = "font-semibold col-start-1 col-span-1 row-start-2 row-span-1 text-slate-700"
SUMMARY_DATA["libraries_tools"] = {
    "label_div": {"label": "Libraries/Tools", "class": className}
}

className = "col-start-2 col-span-1 row-start-2 row-span-1"
SUMMARY_DATA["libraries_tools"]["data_div"] = {"class": className}


# Concepts.
className = "font-semibold col-start-1 col-span-1 row-start-3 row-span-1 text-slate-700"
SUMMARY_DATA["concepts"] = {"label_div": {"label": "Concepts", "class": className}}

className = "col-start-2 col-span-1 row-start-3 row-span-1"
SUMMARY_DATA["concepts"]["data_div"] = {"class": className}


# Website.
className = "font-semibold col-start-1 col-span-1 row-start-4 row-span-1 text-slate-700"
SUMMARY_DATA["website"] = {"label_div": {"label": "Website", "class": className}}

className = "col-start-2 col-span-1 row-start-4 row-span-1"
SUMMARY_DATA["website"]["data_div"] = {"class": className}


# Markdown -----------------------------------------------------------------------------
MARKDOWN: dict[str, str] = dict()

className = "pb-10"
MARKDOWN["class"] = className


# Layout -------------------------------------------------------------------------------
LAYOUT: dict[str, Any] = dict()

className = "bg-[url('/assets/images/math.png')] bg-center bg-cover xl:bg-bottom flex h-[calc(100vh-4rem-2.5rem)] flex-col items-center md:h-[calc(100vh-1.75rem)] overflow-auto"
LAYOUT["class"] = className

# Prose container.
className = """prose prose-slate max-w-full px-4 py-6 backdrop-blur-[4px]
xs:prose-lg lg:prose-xl marker:text-slate-500 prose-headings:text-slate-700 prose-h1:text-center
hover:prose-a:text-slate-500 prose-img:border prose-img:border-slate-400
prose-img:shadow-md prose-img:shadow-slate-400 xs:px-8 xs:prose-h1:text-4xl sm:max-w-xl
md:max-w-2xl lg:max-w-3xl lg:prose-h1:text-5xl lg:prose-h1:leading-tight"""
LAYOUT["div"] = {"class": className}

# Hr.
className = "not-prose mx-2 mt-2 mb-12 border-slate-400"
LAYOUT["hr"] = {"class": className}
