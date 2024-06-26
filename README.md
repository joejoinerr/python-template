# Python template

A starter template for Python projects. Includes lots of useful tools and configurations suitable for most Python 
projects.

## How to use:

1. Clone this repository

```bash
git clone git@github.com:joejoinerr/python-template.git ./my-new-project
```

2. Replace git repository

```bash
cd my-new-project
rm -rf .git
git init
```

3. Update pyproject.toml with your project details
4. Install dependencies

```bash
poetry install
```

5. Install pre-commit hooks

```bash
poetry run pre-commit install
```
