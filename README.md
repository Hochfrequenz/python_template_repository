# Python Template Repository including a `tox.ini`, Unittests&Coverage, Pylint & MyPy Linting Actions and a PyPI Publishing Workflow

<!--- you need to replace the `organization/repo_name` in the status badge URLs --->

![Unittests status badge](https://github.com/Hochfrequenz/python_template_repository/workflows/Unittests/badge.svg)
![Coverage status badge](https://github.com/Hochfrequenz/python_template_repository/workflows/Coverage/badge.svg)
![Linting status badge](https://github.com/Hochfrequenz/python_template_repository/workflows/Linting/badge.svg)
![Black status badge](https://github.com/Hochfrequenz/python_template_repository/workflows/Formatting/badge.svg)

This is a template repository.
It doesn't contain any useful code but only a minimal working setup for a Python project including:

- a basic **project structure** with
  - tox.ini
  - `pyproject.toml` where the project metadata and dependencies are defined
  - and a requirements.txt derived from it
  - an example class
  - an example unit test (using pytest)
- ready to use **Github Actions** for
  - [pytest](https://pytest.org)
  - [code coverage measurement](https://coverage.readthedocs.io) (fails below 80% by default)
  - [pylint](https://pylint.org/) (only accepts 10/10 code rating by default)
  - [mypy](https://github.com/python/mypy) (static type checks where possible)
  - [black](https://github.com/psf/black) code formatter check
  - [isort](https://pycqa.github.io/isort/) import order check
  - [codespell](https://github.com/codespell-project/codespell) spell check (including an ignore list)
  - autoresolve dev-dependencies with `tox -e compile_requirements`
  - ready-to-use publishing workflow for pypi (see readme section below)

By default, it uses Python version 3.13.

This repository uses a [`src`-based layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/).
This approach has many advantages and basically means for developers, that all business logic lives in the `src` directory.

## How to use this Repository on Your Machine

### Installation of Tox / Creating the tox base venv
If you ever set up your toxbase virtual environment already, skip this first step and continue with the project-specific setup.

<details>
<summary>
 Creating the toxbase from scratch (windows)
</summary>

You can either follow the [installation instructions](https://tox.readthedocs.io/en/latest/installation.html)) and that a `.toxbase` environment has been created.
Here we repeat the most important steps.

#### Enure you are allowed to execute scripts in powershell (Windows only)
On new Windows machines it is possible that the execution policy is set to restricted and you are not allowed execute scripts. You can find detailed information [here](https://learn.microsoft.com/de-de/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.3).

The quickest way to solve this problem: Open an Administrator Powershell (e.g. Windows PowerShell App, right click: 'Run as Adminstrator')
```ps
Set-ExecutionPolicy -ExecutionPolicy AllSigned
```
Then close the admin powershell and continue in the regular shell.

#### Create the `.toxbase` environment
`.toxbase` is a project independent virtual environment-template for all the tox environments on your machine. If anything is weird during the tox installation or after the installation, try turning your computer off and on again before getting too frustrated.
Ask your Hochfrequenz colleagues for help.

```ps
# Change to your user directory, create tools directory if it does not exist
$ cd C:\Users\YourUserName
# Create a virtual environment called .toxbase
$ python -m venv .toxbase
```

then
```ps
# Windows Powershell
$ .\.toxbase\Scripts\Activate.ps1
# XOR Windows default (e.g. cmder)
λ .toxbase\Scripts\activate.bat
# the virtual environment is active
# if you see the environment name at the beginning of the line
(.toxbase) $ python -m pip install --upgrade pip
(.toxbase) $ pip install tox
(.toxbase) $ tox --version
```

#### Add the toxbase interpreter to the Path environment variable
Finally, we need to make the tox command available in all future terminal sessions.
There are ways to achieve this goal using only the powershell commands, but we just use the "regular" way:

* Type systemvariable in the search field of your windows taskbar.
* Click on Edit system variables, then on environment variables.
* In the next window select Path in the upper part (User variables for YourUserName) and click on edit.
* Add a new path with `C:\Users\YourUserName\.toxbase\Scripts\`
  * ⚠️ You have to replace YourUserName with your actual username in the path!
     the path up to .toxbase has already been printed to the CLI in the tox --version command above

* Save the settings.
* Now you have to sign out and in again to make the changes work.

You should now be able to type the following and get a reasonable answer
```
tox --version
```
in every shell, no matter if you activated the toxbase again.

#### Umlaute in Paths
Tox has an issue if you have an umlaut in your username. [This issue](https://github.com/tox-dev/tox/issues/1550#issuecomment-727824763) is well known.

To solve it you have to add another environment variable `PYTHONIOENCODING` with the value `utf-8` ([source](https://github.com/tox-dev/tox/issues/1550#issuecomment-1011952057)).

Start a new PowerShell session and try to run tox -e dev in your repository again.

</details>

<details>
<summary>
 Creating the toxbase from scratch (unix)
</summary>
Open a terminal and execute the following commands

```sh
# Change to your user directory
$ cd ~
# Create a virtual environment called .toxbase
$ python -m venv .toxbase
```
Now we activate the virtual environment, update pip and install tox:

```
$ source .toxbase/bin/activate
# the virtual environment is active
# if you see the environment name at the beginning of the line
(.toxbase) $ python -m pip install --upgrade pip
(.toxbase) $ pip install tox
(.toxbase) $ tox --version
```
Create a new folder bin in the home directory and add a symbolic link inside
```
cd
# create a `bin` directory
mkdir bin
# set link to ~/bin/tox
ln -s ~/.toxbase/bin/tox ~/bin/tox
```
Set the PATH variable

```
cd
# open the config file .bashrc
nano .bashrc
# Go to the bottom of the file and insert
# make tox accessible in each session from everywhere
PATH = "${HOME}/bin:${PATH}"
export PATH
# save and close the file with CTRL+O and CTRL+X
```
#### fish
```
cd
# open the config.fish file
nano ~/.config/fish/config.fish
# Go to the bottom of the file and insert
# make tox accessible in each session from everywhere
set PATH {$HOME}/bin $PATH
# save and close the file with CTRL+O and CTRL+X
```
Check if everything works by opening a new terminal window and run
```bash
tox --version
```

</details>

### Creating the project-specific dev environment.
If tox is set up, you're ready to start:
   1. clone the repository, you want to work in
   2. create the `dev` environment on your machine. To do this:
       a) Open a Powershell
       b) change directory to your repository
and finally type

```bash
tox -e dev
```

You have now created the development environment (dev environment). It is the environment which contains both the usual requirements as well as the testing and linting tools.

### How to use with PyCharm

1. You have cloned the repository, you want to work in, and have created the virtual environment, in which the repository should be executed (`your_repo/.tox/dev`). Now, to actually work inside the newly created environment, you need to tell PyCharm (your IDE) that it should use the virtual environment - to be more precise: the interpreter of this dev environment. How to do this:
a) navigate to: File ➡ Settings (Strg + Alt + S) ➡ Project: your_project ➡ Python Interpreter ➡ Add interpreter ➡ Existing
b) Choose as interpreter: `your_repo\.tox\dev\Scripts\python.exe` (under windows)
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
2. **Select the python interpreter** ([official docs](https://code.visualstudio.com/docs/python/environments#_manually-specify-an-interpreter)) which is created by tox. Open the command pallett with `CTRL + P` and type `Python: Select Interpreter`. Select the interpreter which is placed in `.tox/dev/Scripts/python.exe` under Windows or `.tox/dev/bin/python` under Linux and macOS.
3. **Set up pytest and pylint**. Therefore we open the file `.vscode/settings.json` which should be automatically generated during the interpreter setup. If it doesn't exist, create it. Insert the following lines into the settings:

```json
{
  "python.testing.unittestEnabled": false,
  "python.testing.nosetestsEnabled": false,
  "python.testing.pytestEnabled": true,
  "pythonTestExplorer.testFramework": "pytest",
  "python.testing.pytestArgs": ["unittests"],
  "python.linting.pylintEnabled": true
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

1. Fill out the metadata in the [`pyproject.toml`](pyproject.toml); Namely the package name and the dependencies which should be in sync with your `requirements.in`.
2. Uncomment the lines in [`.github/workflows/python-publish.yml`](.github/workflows/python-publish.yml)
3. Create a [new environment in your GitHub repository](https://github.com/Hochfrequenz/python_template_repository/settings/environments) and call it `release`.
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
