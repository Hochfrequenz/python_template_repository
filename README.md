# python_repo_template

This is a template repository. It doesn't contain any actual code but only a basic setup for a Python project including:

+ a basic **project structure** with
    + tox.ini
    + requirements.in
    + and a requirements.txt derived from it
    + an example class
    + an example unit test (using pytest)
+ ready to use **Github Actions** for
    + [pytest](https://pytest.org)
    + [code coverage measurement](https://coverage.readthedocs.io) (fails below 80% by default)
    + [pylint](https://pylint.org/) (only accepts 10/10 code rating by default)
    + [black](https://github.com/psf/black) code formatter check
      using [lgeiger/black-action](https://github.com/lgeiger/black-action)

By default it uses Python version 3.9.

## How to use this Repository on Your Maschine

This introduction assumes that you have tox installed already (
see [installation instructions](https://tox.readthedocs.io/en/latest/install.html)) and that a `.toxbase` environment
has been created.

If this is the case, clone this repository and create the `dev` environment on your maschine.

```bash
tox -e dev
```

### How to use with PyCharm

1. Create a new project using existing sources with your local working copy of this repository as root directory. Choose
   the path `your_repo/.tox/dev/` as path of the "previously configured interpreter".
2. Set the
   default [test runner of your project](https://www.jetbrains.com/help/pycharm/choosing-your-testing-framework.html) to
   pytest.
3. Set
   the [working directory of the unit tests](https://www.jetbrains.com/help/pycharm/creating-run-debug-configuration-for-tests.html)
   to the project root (instead of the unittest directory)

### How to user with VS Code

_please add docs here_
