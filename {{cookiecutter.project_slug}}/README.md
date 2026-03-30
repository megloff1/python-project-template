# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Installation

```bash
uv sync
```

## Usage

```python
import {{ cookiecutter.package_name }}
```

## Development

```bash
# Run tests
uv run pytest

# Lint
uv run ruff check .

# Format
uv run ruff format .
```
{%- if cookiecutter.license != "None" %}

## License

This project is licensed under the {{ cookiecutter.license }} License — see the [LICENSE](LICENSE) file for details.
{%- endif %}
