# Data Project Workflows

### How to Use this Guide
- This guide contains several workflow patterns for different aspects of a data project that has a set up based on the instructions found in *[Data Project Creation/Installation Instructions](/data_project_installation_instructions.md)*:
	- There is a dev tools script `tools.sh` located in the project's root directory
	- The directory structure of the project is of the following form (note that some directories might be missing if they're not needed for the given project):
		<div align="center">
			<img src="images/top_level_project_directory_tree_scaled.svg" />
		</div>
	- (Optionally) There is an app located in the `src` folder that is set up with `tailwind`
- Some of the workflow patterns are done only once overall or once per project; others can be done multiple times per project. The patterns that are only done once overall or once per project will be noted as such in parentheses. The remaining patterns can be done multiple times.
- This guide is not meant to be read in its entirety, it is primarily a reference. To use, just skip around to the topics you need using the section links.

### Topics
- The following section links are listed in order of likely frequency of use:
	- [Dev Tools](#dev-tools)
	- [Dash App (Plotly Dash Website)](#dash-app-plotly-dash-website)
	- [Git](#git)
	- [Python Environment](#python-environment)
	- [Jupyter Lab Settings](#jupyter-lab-settings)
	- [Extras](#extras)

<hr>

### Dev Tools
#### Run Dev Tool Script
- Current dev tools:
	- `black` - code formatter
	- `blacken-docs` - code formatter for markdown code blocks. Not run by default, see the `-md|--markdown` or `-mdo|--markdown-only` CLI options
	- `isort` - import formatter
	- `interrogate` - docstring coverage
	- `flake8` - linter
	- `mypy` - type checker
- By default, `tools.sh` ran with no options will run these dev tools on jupyter notebooks only. The script looks for these files in the directory in which the script is ran and in the sub-directories of that directory recursively
- Additionally, CLI options can apply these tools to python and markdown files and also allow for the skipping of tools during run time
- To see all the CLI options made available by `tools.sh`, use the following command to access the help information:
	- From the project's root directory:
		```shell
		./tools.sh --help
		```
	- From the `src` or `notebooks` directory (or any other directory at that level):
		```shell
		../tools.sh --help
		```
- When using the `-md|--markdown` or `-mdo|--markdown-only` options, a file path(s) to a markdown file(s) must be provided
- When using the `-s|--skip` option, you must provide at least one tool name to skip
- When using the `-t|--type` option, you must provide either `all` or `py` as the argument
- Run the dev tools script:
	- From the project's root directory:
		```shell
		./tools.sh
		```
	- From the `src` or `notebooks` directory (or any other directory at that level):
		```shell
		../tools.sh
		```

[Return to Topics Section](#topics)

<hr>

### Dash App (Plotly Dash Website)
#### Install Node JS (done once overall before creating or collaborating on any projects)

1. Install `node.js` from [https://nodejs.org/en/](https://nodejs.org/en/) (most recent is fine)

#### Install the javascript dependencies necessary to run `tailwind` (done once per project)

1. navigate to the project's `src` folder
1. Use the following command to install the dependencies found in `package.json`
	```shell
	npm install
	```
#### Running the App
- Running the app requires two bash commands that will run two processes continuously to serve the app and serve its styles and update the app when changes are made
1. Run the `tailwind` compile script:
	1. navigate to the project's `src` folder
	1. run the compile script:
		```shell
		./tailwind_compile.sh
		```
1. In a separate terminal, run the app with a dev server:
	1. navigate to the project's `src` folder
	1. run the app:
		```shell
		python app.py
		```

#### Adding Styles
- There are three main places where style information can be added to the app and its components:
	1. `tailwind` utility classes within Dash components using the `className` parameter
	1. Extending/modifying `tailwind` styles using the `tailwind.config.js` file. See the `tailwind` documentation to learn more.
	1. Adding CSS directly to the `input.css` file that gets compiled to an `output.css` file via the `tailwind_compile.sh` script. The `input.css` file is found at `src > assets > css > src`. See the `tailwind` documentation to learn how to add CSS styles to this file into the correct layers

[Return to Topics Section](#topics)

<hr>

### Git
- git/GitHub workflows to be added in the future

[Return to Topics Section](#topics)

<hr>

### Python Environment
#### Adding/Removing Packages
- `pip` packages will be preferred over `conda` packages. Only install `conda` packages if there is no `pip` equivalent
- Add packages:
	```shell
	poetry add <package_name>=<version_constraint>
	```
	- the `version_constraint` is optional
	- use this command in place of `pip install <package_name>=<version_constraint>`

- Add packages to a group (for an explanation of groups and to create a group, see the *[Dependency Groups Within `pyproject.toml`](#dependency-groups-within-pyprojecttoml)* section):
	```shell
	poetry add <package_name>=<version_constraint> --group <group_name>
	```
	- Useful for separating dependencies in the `pyproject.toml` file into logical groups such as grouping the development dependencies together or the test dependencies together
	> For how to specify version constraints, see the "Version constraints" section of Poetry's [dependency specification](https://python-poetry.org/docs/dependency-specification/)
- Remove packages:
	```shell
	poetry remove <package_name>
	```

#### Updating environment when `environment.yml` changes
1. Activate the environment that you're planning to update:
	```shell
	conda activate <env_name>
	```
2. Update the environment based on the new `environment.yml` file:
	```shell
	conda env update --file environment.yml --prune
	```
	- `--prune` will make sure any dependencies that were removed from `environment.yml` will be uninstalled from the environment.

#### Updating environment when `pyproject.toml` changes
- To install dependencies when there has been an update or change to the `pyproject.toml` or `poetry.lock` file (i.e. when we add a new package(s) to the `pyproject.toml` file):
	```shell
	poetry install
	```
	- If you don't notice a change and you get errors when you start working, you might just need to run this command to install packages that have been recently added by another collaborator

#### Update `environment.yml` when `conda` packages are added
- Activate the environment that you want to update the `environment.yml` file for:
	```shell
	conda activate <env_name>
	```
- Write the new changes to the `environment.yml` file with:
	```shell
	conda env export --from-history | grep -v "^prefix: " > environment.yml
	```
	- `--from-history` will ensure that only the dependencies that we manually added to the `conda` environment will get written in the `environment.yml` file

[Return to Topics Section](#topics)

<hr>

### Jupyter Lab Settings
#### Add a Python Environment to Jupyter/Jupyter Lab (done once per environment)
- activate `<env_name>` environment:
	```shell
	conda activate <env_name>
	```
- install the environment in Jupyter:
	```shell
	python -m ipykernel install --user --name <env_name>
	```

#### Install Jupyter Lab Contextual Help Prettier (done once per environment)
- Install the two packages below to add nice contextual help for a given environment (make sure to have `jupyterlab-pygments` installed. Check to see if it is with `poetry show jupyterlab-pygments`):
	```shell
	# Install sphinx
	poetry add sphinx
	```
	```shell
	# Install docrepr
	poetry add docrepr
	```
- Access the contextual help by placing you cursor in a class/function/method or other object (click the text to place the cursor) and then use the keyboard shortcut `ctrl`+`I`.

[Return to Topics Section](#topics)

<hr>

### Extras

#### Dependency Groups Within `pyproject.toml`
- Think of dependency groups as labels associated with your dependencies, they are simply a way to organize the dependencies logically
- The main dependency group is the section with the heading `[tool.poetry.dependencies]`, all dependencies that are needed to **run** the project must be here
- Other dependency groups (ones that you add yourself) must only contain dependencies you need for development of the project (things like formatters, linters, unit testing libraries, etc.)
- Add a dependency group by editing the `pyproject.toml` file directly, follow the following format which adds a heading:
	```toml
	[tool.poetry.group.<group_name>.dependencies]
	```
- If the plan is to leave the development dependencies in one all encompassing group, a common group name would be `dev`, see the example `pyproject.toml` code block below. Otherwise, you could separate the development dependencies into however many groups that you want. Poetry even allows for installing or synchronizing by groups, so multiple groups for different purposes could be useful


#### Example `pyproject.toml`
- The required fields below get set when `poetry init` is called during project setup but can also be modified afterwards by editing `pyproject.toml` directly
- If there is a `packages` attribute in the `[tool.poetry]` section, remove it. These projects will not be packages

```toml
[tool.poetry]
name = "dash-test" # Required (non-null)
version = "0.1.0" # Required (non-null)
description = "" # Required (non-null)
authors = ["Joe Shmow <joeshmow@gmail.com>"] # Required
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.9"
dash = "^2.7.0"
ibis-framework = { version = "^3.2.0", python = ">=3.9,<3.11" }

[tool.poetry.group.dev.dependencies]
pytest = "^6.0.0"
pytest-mock = "*"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

#### Some Reasons for a Conda + Poetry Setup
- "freeze" type approaches require more manual upkeep of the dependencies file. 2 dependency files (2 non lock files) need to be maintained, one for "production" and one for "development"
- if a project uses conda and you plan to host it online as a website there are fewer hosting services with conda buildpacks (the software that sets up the environment to run your website on a cloud server)
- pypi packages (installed via poetry) are often more up-to-date, usually by a couple months
- in the end, having both allows for packages from either conda, conda-forge, or pypi
- conda can be slow
- poetry's dependency resolver is more advanced than pip's
- poetry, compared to other python environment/dependency managers, seems to have consistent activity on its GitHub and is actively being maintained