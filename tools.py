"""A CLI for running development tools on jupyter notebooks and python files."""

import subprocess

import click

# Help messages and meta variables for the CLI options and arguments.
help_msg = {
    "markdown_help": "Runs blacken-docs on FILENAME to format code blocks within.",
    "skip_help": """Skips application of the tool names provided. The value is a
    string containing space separated tool names""",
    "skip_metavar": "STRING",
    "file_type_help": """'nb' - Runs tools on jupyter notebooks (.ipynb) only.
    'all' - Runs tools on both jupyter notebooks and python files (.ipynb and .py).
    'py' - Runs tools on python files (.py) only.""",
    "filenames_metavar": "[FILENAME]...",
}


@click.command()
@click.option("-md", "--markdown", is_flag=True, help=help_msg["markdown_help"])
@click.option(
    "-s",
    "--skip",
    help=help_msg["skip_help"],
    metavar=help_msg["skip_metavar"],
)
@click.option(
    "-ft",
    "--file-type",
    type=click.Choice(["nb", "py", "all"]),
    show_default=True,
    default="nb",
    help=help_msg["file_type_help"],
)
@click.argument(
    "filenames",
    nargs=-1,
    type=click.Path(exists=True, dir_okay=False),
    metavar=help_msg["filenames_metavar"],
)
def tools(
    markdown: bool,
    skip: str | None,
    file_type: str,
    filenames: tuple[str, ...],
) -> None:
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
                  see the -md|--markdown cli option.
           isort: import formatter
     interrogate: docstring coverage
          flake8: linter
            mypy: type checker
    """
    # Constants ------------------------------------------------------------------------
    run_tools = ["black", "blacken-docs", "isort", "interrogate", "flake8"]
    header_banner_len = 80
    tool_banner_len = 74
    type_messages = {
        "nb": "notebooks (.ipynb)",
        "py": "python files (.py)",
        "md": "markdown files (.md)",
    }
    type_prepend = {}

    # Helper Functions -----------------------------------------------------------------
    def double_echo(func):
        """Decorate banners with two blank lines on each side."""

        def wrapper_double_echo(*args, **kwargs):
            """Add a blank line before and after the func call."""
            click.echo("")
            func(*args, **kwargs)
            click.echo("")

        return wrapper_double_echo

    @double_echo
    def create_banner(
        message: str,
        *,
        banner_length: int,
        type_prepend: dict[str, str],
        fg_color: str,
        bg_color: str,
        file_type: str | None = None,
    ) -> None:
        """Create a banner with a message and coloring for clarity.

        If `file_type` is not specified, the banner is a header banner and no file type
        is prepended to the banner. If `file_type` is specified, the banner is a tool
        banner thus the file type that the tool is running on will be prepended to the
        banner.

        Parameters
        ----------
        message : str
            Banner message.
        banner_length : int
            Length of banner in number of characters.
        type_prepend : dict[str, str]
            Mapping from `file_type` string to the prepend string.
        fg_color : str
            Foreground color (text color).
        bg_color : str
            Background color.
        file_type : str | None, optional
            Type of file that the tool is being run on, by default None
        """
        # Calculate whitespace in order to center the banner message.
        total_ws = banner_length - len(message)
        left_ws = total_ws // 2
        right_ws = total_ws - left_ws

        if file_type:
            # Calculate new left whitespace to allow room for prepended file type.
            left_ws = left_ws - len(type_prepend[file_type]) - 1
            banner_message = (
                f" {type_prepend[file_type]}{' '*left_ws}{message}{' '*right_ws}"
            )
        else:
            banner_message = f"{' '*left_ws}{message}{' '*right_ws}"
        click.echo(click.style(banner_message, fg=fg_color, bg=bg_color))

    def generate_run_summary(
        tools: list[str], prepend: dict[str, str], type: str
    ) -> None:
        """Generate a summary of the run including the tools and file type being run on.

        Parameters
        ----------
        tools : list[str]
            List of development tools selected for the current run.
        prepend : dict[str, str]
            Mapping from `file_type` string to the prepend string.
        type : str
            File type for the current run.
        """
        # Remove blacken-docs from the list of tools shown for python files.
        if type == "py":
            tools_display = [tool for tool in tools if tool != "blacken-docs"]
        else:
            tools_display = tools

        click.echo("Run Summary:")
        if len(tools_display) == 1:
            click.echo(f"Tool(s): {tools_display[0]}")
        else:
            click.echo(f"Tool(s): {', '.join(tools_display)}")
        click.echo(f"File Type(s): {', '.join(prepend.values())}")

    # Input Validation -----------------------------------------------------------------
    if markdown and not filenames:
        raise click.UsageError(
            "No FILENAME provided for markdown option. Provide one or more FILENAME as "
            + "an argument."
        )

    if (skip or (file_type != "nb")) and markdown:
        raise click.UsageError(
            "The markdown option can only be run without any other options."
        )

    # Input Processing -----------------------------------------------------------------
    if markdown:
        run_tools = ["blacken-docs"]
        type_prepend["md"] = type_messages["md"]
        file_type = "md"
    elif file_type == "all":
        type_prepend["nb"] = type_messages["nb"]
        type_prepend["py"] = type_messages["py"]
    else:
        type_prepend[file_type] = type_messages[file_type]

    if skip:
        skip_tools = set(skip.split(" "))
        for tool in skip_tools:
            if tool not in run_tools:
                raise click.BadParameter(f"'{tool}' is not a current dev tool.")
            else:
                run_tools.remove(tool)

    # Run Dev Tools --------------------------------------------------------------------
    # click.clear()
    create_banner(
        "RUNNING DEV TOOLS",
        banner_length=header_banner_len,
        type_prepend=type_prepend,
        fg_color="black",
        bg_color="bright_cyan",
    )

    generate_run_summary(tools=run_tools, prepend=type_prepend, type=file_type)

    for ft in type_prepend:
        for tool in run_tools:
            if ft == "nb":
                create_banner(
                    f"Running {tool}",
                    banner_length=tool_banner_len,
                    type_prepend=type_prepend,
                    fg_color="black",
                    bg_color="bright_yellow",
                    file_type=ft,
                )
                subprocess.run(["nbqa", tool, "."])
            elif ft == "py":
                if tool != "blacken-docs":
                    create_banner(
                        f"Running {tool}",
                        banner_length=tool_banner_len,
                        type_prepend=type_prepend,
                        fg_color="black",
                        bg_color="bright_green",
                        file_type=ft,
                    )
                    subprocess.run([tool, "."])
            elif ft == "md":
                create_banner(
                    f"Running {tool}",
                    banner_length=tool_banner_len,
                    type_prepend=type_prepend,
                    fg_color="black",
                    bg_color="bright_blue",
                    file_type=ft,
                )
                subprocess.run([tool, " ".join(filenames)])

    create_banner(
        "DEV TOOLS COMPLETE",
        banner_length=header_banner_len,
        type_prepend=type_prepend,
        fg_color="black",
        bg_color="bright_cyan",
    )


if __name__ == "__main__":
    tools()
