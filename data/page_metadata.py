"""Create a json file from the page metadata excel file."""

from pathlib import Path

import pandas as pd
from rich.pretty import pprint

project_dir = Path(__file__).parents[1]
# Path to the project metadata excel file
metadata_path = project_dir / "data/page_metadata.xlsx"
# Path to the location where the json will be stored within the app src folder.
json_path = project_dir / "src/data/page_metadata.json"

data_types = {
    "order": pd.Int8Dtype(),
    "section": pd.StringDtype(),
    "name": pd.StringDtype(),
    "repo": pd.StringDtype(),
    "languages": pd.StringDtype(),
    "libraries_tools": pd.StringDtype(),
    "concepts": pd.StringDtype(),
    "website": pd.StringDtype(),
    "website_name": pd.StringDtype(),
}

projects = pd.read_excel(metadata_path, dtype=data_types, index_col=0)
projects.to_json(json_path, orient="index")

pprint("Excel file path:")
pprint(metadata_path)
pprint("JSON output path:")
pprint(json_path)
