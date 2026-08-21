# Python Template Repository including `uv` tooling, Unittests&Coverage, Ruff & MyPy Linting Actions and a PyPI Publishing Workflow

<!--- you need to replace the `organization/repo_name` in the status badge URLs --->

![Unittests status badge](https://github.com/Hochfrequenz/python_template_repository/workflows/Unittests/badge.svg)
![Coverage status badge](https://github.com/Hochfrequenz/python_template_repository/workflows/Coverage/badge.svg)
![Linting status badge](https://github.com/Hochfrequenz/python_template_repository/workflows/Linting/badge.svg)
![Ruff status badge](https://github.com/Hochfrequenz/python_template_repository/workflows/Formatting/badge.svg)

This is a template repository.
It doesn't contain any useful code but only a minimal working setup for a Python project including:

- a basic **project structure** with
  - `pyproject.toml` where the project metadata, dependencies and [dependency-groups](https://peps.python.org/pep-0735/) are defined
  - a `uv.lock` lockfile derived from it
  - an example class
  - an example unit test (using pytest)
- ready to use **Github Actions** for
  - [pytest](https://pytest.org)
  - [code coverage measurement](https://coverage.readthedocs.io) (fails below 80% by default)
  - [ruff](https://docs.astral.sh/ruff/) lint checks, code formatting and import order (replacing pylint, black and isort)
  - [mypy](https://github.com/python/mypy) (static type checks where possible)
  - [codespell](https://github.com/codespell-project/codespell) spell check (including an ignore list)
  - dependency management and locking with [uv](https://docs.astral.sh/uv/)
  - ready-to-use publishing workflow for pypi (see readme section below)

By default, it uses Python version 3.13.

This repository uses a [`src`-based layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/).
This approach has many advantages and basically means for developers, that all business logic lives in the `src` directory.

## How to use this Repository on Your Machine

### Installing uv
This project uses [uv](https://docs.astral.sh/uv/) to manage the Python interpreter, virtual environment and dependencies.
If you don't have uv installed yet, follow the [official installation instructions](https://docs.astral.sh/uv/getting-started/installation/), e.g.:

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```ps
# Windows Powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Creating the project-specific dev environment
Once uv is installed, you're ready to start:
   1. clone the repository you want to work in
   2. change directory into your local clone
   3. create the dev environment on your machine:

```bash
uv sync --group dev
```

This creates a `.venv` virtual environment in the project root and installs the usual requirements as well as the testing, linting, formatting and type-checking tools (see the `[dependency-groups]` in [`pyproject.toml`](pyproject.toml)).
uv also pins/downloads the right Python interpreter version automatically if it isn't already available on your machine.

### How to use with PyCharm

1. You have cloned the repository, you want to work in, and have created the virtual environment (`your_repo/.venv`), in which the repository should be executed. Now, to actually work inside the newly created environment, you need to tell PyCharm (your IDE) that it should use the virtual environment - to be more precise: the interpreter of this dev environment. How to do this:
a) navigate to: File ➡ Settings (Strg + Alt + S) ➡ Project: your_project ➡ Python Interpreter ➡ Add interpreter ➡ Existing
b) Choose as interpreter: `your_repo\.venv\Scripts\python.exe` (under windows) or `your_repo/.venv/bin/python` (under Linux/macOS)
2. Set the default test runner of your project to pytest. How to do it:
a) navigate to Files ➡ Settings ➡ Tools ➡ Python integrated tools ➡ Testing: Default test runner
b) Change to "pytest"
If this doesn't work anymore, see [the PyCharm docs](https://www.jetbrains.com/help/pycharm/choosing-your-testing-framework.html)
3. Set the `src` directory as sources root. How to do this:
right click on 'src' ➡ "Mark directory as…" ➡ sources root
If this doesn't work anymore, see: [PyCharm docs](https://www.jetbrains.com/help/pycharm/content-root.html).
Setting the `src` directory right, allows PyCharm to effectively suggest import paths.
If you ever see something like `from src.mypackage.mymodule import ...`, then you probably forgot this step.
5. Set the working directory of the unit tests to the project root (instead of the unittest directory). How to do this:
a) Open any test file whose name starts with `test_` in unit tests/tests
b) Right click inside the code ➡ More Run/Debug ➡ Modify Run Configuration ➡ expand Environment collapsible ➡ Working directory
c) Change to `your_repo` instead of `your_repo\unittests`
By doing so, the import and other file paths in the tests are relative to the repo root.
If this doesn't work anymore, see: [working directory of the unit tests](https://www.jetbrains.com/help/pycharm/creating-run-debug-configuration-for-tests.html)

### How to use with VS Code
All paths mentioned in this section are relative to the repository root.

1. Open the folder with VS Code.
2. **Select the python interpreter** ([official docs](https://code.visualstudio.com/docs/python/environments#_manually-specify-an-interpreter)) which is created by uv. Open the command pallett with `CTRL + P` and type `Python: Select Interpreter`. Select the interpreter which is placed in `.venv/Scripts/python.exe` under Windows or `.venv/bin/python` under Linux and macOS.
3. **Set up pytest**. Therefore we open the file `.vscode/settings.json` which should be automatically generated during the interpreter setup. If it doesn't exist, create it. Insert the following lines into the settings:

```json
{
  "python.testing.unittestEnabled": false,
  "python.testing.nosetestsEnabled": false,
  "python.testing.pytestEnabled": true,
  "pythonTestExplorer.testFramework": "pytest",
  "python.testing.pytestArgs": ["unittests"]
}
```

4. Create a `.env` file and insert the following line

For Windows:

```
PYTHONPATH=src;${PYTHONPATH}
```

For Linux and Mac:

```
PYTHONPATH=src:${PYTHONPATH}
```

This makes sure, that the imports are working for the unittests.
At the moment I am not totally sure that it is the best practise, but it's getting the job done.

5. Enjoy 🤗

## Publishing on PyPI

This repository contains all necessary CI steps to publish any project created from it on PyPI.
It uses the trusted publishers workflow as described in the [official Python documentation](https://packaging.python.org/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/).
It just requires some manual adjustments/settings depending on your project:

1. Fill out the metadata in the [`pyproject.toml`](pyproject.toml); Namely the package name and the `dependencies` list.
2. Uncomment the lines in [`.github/workflows/python-publish.yml`](.github/workflows/python-publish.yml)
3. Create a [new environment in your GitHub repository](https://github.com/Hochfrequenz/python_template_repository/settings/environments) and call it `release`.
   If you restrict that environment's deployment branches, you **must** add a rule of type *Tag* matching `v*`.
   A release event deploys from the tag (`refs/tags/v1.2.3`), not from a branch, so an environment that only
   allows the `main` branch rejects every publish - and the job then fails having run no steps at all, which
   gives you nothing to debug from.
4. Set up a new trusted publisher [in your PYPI account](https://pypi.org/manage/account/publishing/).
   1. PyPI Project Name: The name which you defined in the `pyproject.toml` is the name of the project which you have to enter here.
   2. Owner: The GitHub organization name or GitHub username that owns the repository
   3. Repository name: The name of the GitHub repository that contains the publishing workflow
   4. Workflow name: The filename of the publishing workflow. This file should exist in the .github/workflows/ directory in the repository configured above. Here in our case: `python-publish.yml`
   5. Environment name: The name of the GitHub Actions environment that the above workflow uses for publishing. Here in our case: `release`
5. Now create a release by clicking on "Create new release" in the right Github sidebar (or visit `github.com/your-username/your-reponame/releases/new`). This should trigger the workflow (see the "Actions" tab of your repo).
6. Check if the action failed. If it succeeded your PyPI account should now show the new project. It might take some minutes until the package can be installed via `pip install packagename` because the index has to be updated.
7. Now create another PyPI token with limited scope and update the Github repository secret accordingly.

## Contribute

You are very welcome to contribute to this template repository by opening a pull request against the main branch.

### GitHub Actions

- Dependabot auto-approve / -merge:
  - If the actor is the Dependabot bot (i.e. on every commit by Dependabot)
    the pull request is automatically approved and auto merge gets activated
    (using squash merge).
    Note that if you haven't enabled "auto merge" for your repository, the auto merge activation will fail.
    If you want to use a merge type other than "squash merge" you have to edit the workflow.
