# **Dev Tool CLI**

## **Overview of Project**
I created a CLI tool using the `click` python package in order to run the
different development tools that I was using on my portfolio project. The CLI
allows me to choose which file type to run the tools on (jupyter notebook,
python files, or both) and which tools to skip if needed. I can also run tools
directly on markdown files if I supply the file(s) as an argument. For jupyter
notebooks and python files, the CLI will run the tools on the current directory
with support for running on specific files limited to only jupyter notebooks for
now. Currently the tools include:

1. `black` - code formatter
1. `blacken-docs` - code formatter for code blocks in markdown
1. `isort` - import sorter
1. `interrogate` - docstring coverage
1. `flake8` - linting operations
1. `mypy` - type checker

The following is an image showing the CLI help menu:

<div align="center">
    <img src="assets/images/dev_tool_cli/dev_tools_cli_help.svg"
         alt="dev tools cli output: help flag" />
</div>

The output includes a summary of the run including tools applied and the file
types they are applied to. The output also includes the tool name and file type
in colored banners separating the output from each tool. Here is an example
output:

<div align="center">
    <img src="assets/images/dev_tool_cli/dev_tools_cli_py.svg"
         alt="dev tools cli output: type option set to python" />
</div>

## **Future Work**
Currently, the `[FILENAME]` argument is required to be a markdown file or a
jupyter notebook. I would like to add the ability to also pass in python files
so that I can apply the tools individually to that file type as well.
