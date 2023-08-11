"""A CLI for running development tools on jupyter notebooks and python files."""
import subprocess

import click


# Decorator that adds a blank line before and after a tool is run
def double_echo(func):
    """Add blank lines."""

    def wrapper_double_echo(*args, **kwargs):
        """Add a blank line before and after the func call."""
        click.echo("")
        func(*args, **kwargs)
        click.echo("")

    return wrapper_double_echo


@double_echo
def create_banner(message, banner_length, fg, bg):
    """Create a banner with a message and coloring for clarity."""
    whitespace = banner_length - len(message)
    left_ws = whitespace // 2
    right_ws = whitespace - left_ws
    banner_message = f"{' '*left_ws}{message}{' '*right_ws}"
    click.echo(click.style(banner_message, fg=fg, bg=bg))


header_banner_length = 80
tool_banner_length = 70


@click.command()
@click.option(
    "-md",
    "--markdown",
    is_flag=True,
    help="Runs blacken-docs on FILENAME to format code blocks within.",
)
@click.option(
    "-mdo",
    "--markdown-only",
    is_flag=True,
    help="""ONLY runs blacken-docs on FILENAME to format code blocks within. No other
    tools are run.""",
)
@click.option(
    "-s",
    "--skip",
    help="""Skips application of the tool names provided. The value is a string
    containing space separated tool names""",
    metavar="STRING",
)
@click.option(
    "-ft",
    "--file-type",
    type=click.Choice(["nb", "py", "all"]),
    show_default=True,
    default="nb",
    help="""'nb' - Runs tools on jupyter notebooks (.ipynb) only.
    'all' - Runs tools on both jupyter notebooks and python files (.ipynb and .py).
    'py' - Runs tools on python files (.py) only.""",
)
@click.argument(
    "filenames",
    nargs=-1,
    type=click.Path(exists=True, dir_okay=False),
    metavar="[FILENAME]...",
)
def tools(markdown, markdown_only, skip, file_type, filenames):
    """tools.py runs development tools on project files.

    tools.py can be run from either the project root directory or any of the first level
    directories within the root. The default behavior is to run these tools on jupyter
    notebooks (.ipynb) only. CLI options allow for modifying this behavior to be able to
    run these tools on python and markdown files as well. Additionally, there is an
    option to allow for skipping tools during the run process if needed.

    Current Tools In Use:

    \b
           black: code formatter
    blacken-docs: code formatter for markdown code blocks. Not run by default,
                  see the -md|--markdown or -mdo|--markdown-only cli options.
           isort: import formatter
     interrogate: docstring coverage
          flake8: linter
            mypy: type checker
    """
    run_tools = ["black", "isort", "interrogate", "flake8"]

    click.echo("------------ options ------------")
    click.echo(f"markdown: {markdown}")
    click.echo(f"markdown_only: {markdown_only}")
    click.echo(f"skip: {skip}")
    click.echo(f"file_type: {file_type}")
    click.echo("---------- end options ----------\n\n")

    click.echo("----------- arguments -----------")
    if filenames:
        click.echo(f"filename: {' '.join(filenames)}")
    else:
        click.echo("filenames:")
    click.echo("--------- end arguments ---------\n\n")

    # Input Validation -----------------------------------------------------------------
    if markdown and markdown_only:
        raise click.UsageError(
            "Two markdown options were used. Only one can be used at a time."
        )

    if (skip or (file_type != "nb")) and markdown_only:
        raise click.UsageError(
            "The markdown-only option can only be run without any other options."
        )

    if markdown or markdown_only:
        if not filenames:
            raise click.UsageError(
                "No FILENAME provided. Provide one or more FILENAME as an argument."
            )

    # Input Processing -----------------------------------------------------------------
    if markdown:
        run_tools.append("blacken-docs")

    if markdown_only:
        run_tools = ["blacken-docs"]

    if skip:
        skip_tools = set(skip.split(" "))
        for tool in skip_tools:
            if tool not in run_tools:
                raise click.BadParameter(f"'{tool}' is not a current dev tool.")
            else:
                run_tools.remove(tool)

    # Run Dev Tools --------------------------------------------------------------------
    click.clear()
    create_banner(
        "RUNNING DEV TOOLS", header_banner_length, fg="black", bg="bright_cyan"
    )

    click.echo(f"Tools to Run: {run_tools}")

    if file_type == "all":
        file_type = ["nb", "py"]
    else:
        file_type = [file_type]

    for ft in file_type:
        for tool in run_tools:
            if ft == "nb":
                create_banner(
                    f"Running {tool}", tool_banner_length, fg="black", bg="bright_green"
                )
                subprocess.run(["nbqa", tool, "."])
            elif ft == "py":
                if tool != "blacken-docs":
                    create_banner(
                        f"Running {tool}",
                        tool_banner_length,
                        fg="black",
                        bg="bright_blue",
                    )
                    subprocess.run([tool, "."])

    create_banner(
        "DEV TOOLS COMPLETE", header_banner_length, fg="black", bg="bright_cyan"
    )


if __name__ == "__main__":
    tools()
