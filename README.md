# Cookiecutter Python Project (uv + pytest + ruff + mypy)

A [cookiecutter](https://github.com/cookiecutter/cookiecutter) template for modern Python projects using **uv** for dependency management, **pytest** for testing, **ruff** for linting/formatting, and **mypy** for static type checking. First-class support for both **PyCharm** and **VSCode**.

## Prerequisites

### 1. Install uv

[uv](https://docs.astral.sh/uv/) is used for Python and dependency management.

**Linux / macOS:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Homebrew (macOS / Linux):**

```bash
brew install uv
```

**Windows (winget):**

```powershell
winget install --id=astral-sh.uv -e
```

**pip (all platforms):**

```bash
pip install uv
```

**Conda (all platforms):**

```bash
conda install -c conda-forge uv
```

**apt (Debian / Ubuntu):**

See the [official docs](https://docs.astral.sh/uv/getting-started/installation/) for adding the Astral APT repository.

### 2. Install cookiecutter

[cookiecutter](https://github.com/cookiecutter/cookiecutter) generates projects from this template.

**All platforms (recommended — uses uv):**

```bash
uv tool install cookiecutter
```

**pip (all platforms):**

```bash
pip install --user cookiecutter
```

**Homebrew (macOS / Linux):**

```bash
brew install cookiecutter
```

**apt (Debian / Ubuntu):**

```bash
sudo apt install cookiecutter
```

**Conda (all platforms):**

```bash
conda install -c conda-forge cookiecutter
```

## Quick Start

```bash
# Generate a new project
cookiecutter gh:megloff1/python-project-template  # from GitHub
# or
cookiecutter /path/to/this/template     # from local clone

# Enter the project
cd my-project

# Install dependencies
uv sync

# Run tests
uv run pytest

# Lint & format
uv run ruff check .
uv run ruff format --check .

# Type check
uv run mypy src/
```

## Template Variables

| Variable | Default | Description |
|---|---|---|
| `project_name` | `My Project` | Human-readable project name |
| `project_slug` | *(derived)* | Kebab-case slug (directory & PyPI name) |
| `package_name` | *(derived)* | Snake_case Python package name |
| `description` | `A short description` | Brief project description |
| `author_name` | `Your Name` | Author's full name |
| `author_email` | `your@email.com` | Author's email address |
| `python_version` | `3.12` | Python version (`3.12` or `3.13`) |
| `license` | `MIT` | License type (`MIT`, `Apache-2.0`, `GPL-3.0`, or `None`) |
| `ci_provider` | `GitHub` | CI provider (`GitHub`, `GitLab`, `Both`, or `None`) |

## Generated Project Structure

```
my-project/
├── .github/workflows/ci.yml   # GitHub Actions CI (if GitHub/Both)
├── .gitlab-ci.yml              # GitLab CI (if GitLab/Both)
├── .idea/
│   ├── runConfigurations/
│   │   ├── All_Tests.xml       # PyCharm pytest run config
│   │   └── Debug_Main.xml      # PyCharm debug run config
│   ├── modules.xml             # PyCharm module config
│   └── my-project.iml          # Source roots + test runner
├── .vscode/
│   ├── extensions.json         # Recommended extensions
│   ├── launch.json             # Debug configurations
│   └── settings.json           # Ruff + pytest + mypy config
├── src/my_project/
│   ├── __init__.py             # Package with __version__
│   └── py.typed                # PEP 561 marker
├── tests/
│   ├── __init__.py
│   └── test_example.py         # Sample passing test
├── .editorconfig               # Consistent formatting
├── .gitattributes              # Enforce LF line endings (Windows safety)
├── .gitignore                  # Python + uv + IDE
├── .python-version             # uv Python pin
├── LICENSE                     # Based on license choice
├── README.md
└── pyproject.toml              # Single source of truth
```

## Creating a Remote Repository

After generating your project, you may want to push it to a remote Git hosting service.

### GitHub

```bash
cd my-project

# Create a public repo and push (requires gh CLI: https://cli.github.com/)
gh repo create my-project --public --source=. --remote=origin --push

# Or create a private repo
gh repo create my-project --private --source=. --remote=origin --push
```

If you prefer to create the repo manually:

```bash
cd my-project

# 1. Create a new repository on https://github.com/new
# 2. Add the remote and push
git remote add origin git@github.com:YOUR_USERNAME/my-project.git
git branch -M main
git push -u origin main
```

### GitLab

```bash
cd my-project

# Using glab CLI (https://gitlab.com/gitlab-org/cli)
glab repo create my-project --public
git remote add origin git@gitlab.com:YOUR_USERNAME/my-project.git
git branch -M main
git push -u origin main

# Or create a private repo
glab repo create my-project --private
git remote add origin git@gitlab.com:YOUR_USERNAME/my-project.git
git branch -M main
git push -u origin main
```

If you prefer to create the repo manually:

```bash
cd my-project

# 1. Create a new project on https://gitlab.com/projects/new
# 2. Add the remote and push
git remote add origin git@gitlab.com:YOUR_USERNAME/my-project.git
git branch -M main
git push -u origin main
```

## IDE Support

### VSCode

Open the generated project and you'll be prompted to install the recommended extensions:

| Extension | Purpose |
|---|---|
| [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) | Core Python language support |
| [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) | Fast IntelliSense and type information |
| [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff) | Linting and formatting on save |
| [Mypy Type Checker](https://marketplace.visualstudio.com/items?itemName=ms-python.mypy-type-checker) | Static type checking (strict mode) |
| [uv](https://marketplace.visualstudio.com/items?itemName=astral-sh.uv) | uv environment and dependency management |

**Testing** — Pytest is pre-configured. Tests appear in the Testing sidebar (`Ctrl+Shift+;`). Click any test to run or debug it with breakpoints.

**Debugging** — Three launch configurations are included (accessible via `Run and Debug` or `F5`):

- **Debug: Current File** — runs the active `.py` file under the debugger
- **Debug: Module** — runs the package as `python -m <package_name>`
- **Debug: Tests** — runs `pytest tests/ -v` under the debugger

All configurations set `PYTHONPATH` to `src/` so imports resolve correctly with the `src` layout.

**Type Checking** — Mypy runs in strict mode. The VS Code extension reports type errors inline as you edit. Configuration lives in `pyproject.toml` under `[tool.mypy]`.

**Interpreter** — The default interpreter is set to the `.venv` directory, which is where `uv sync` creates the virtual environment. VS Code will auto-detect the correct Python binary (`.venv/bin/python` on macOS/Linux, `.venv\Scripts\python.exe` on Windows) after running `uv sync`.

### PyCharm (2024.3+)

Open the project and PyCharm will detect the uv-managed environment. Install the [Ruff plugin](https://plugins.jetbrains.com/plugin/20574-ruff) from the marketplace for linting/formatting support. Pre-configured run configurations are available in the Run dropdown:

- **All Tests** — runs pytest on the `tests/` directory
- **Debug Main** — run/debug the main package entry point

Test runner, source roots, and `.editorconfig` work out of the box.

## License

This template is released under the MIT License.
