# Python template

A starter template for Python projects. Includes lots of useful tools and
configurations suitable for most Python projects.

## Features

- **Modern Python setup** with `uv` for fast dependency management
- **Type safety** with comprehensive type hints and modern Python 3.9+ syntax
- **Code quality tools**:
  - Pre-commit hooks for automated code formatting and linting
  - Comprehensive linting and formatting configuration
- **Project structure**:
  - Choose between a package or application project structure with `src` layout
  - Well-organized source layout with proper package structure
  - Settings management with `pydantic-settings`
  - Structured logging configuration
  - Utility functions and testing setup
- **Development workflow**:
  - `justfile` for common development tasks
  - Automated dependency installation and environment setup
  - Git integration with initial commit and pre-commit hook installation
- **Best practices**:
  - Google-style docstrings
  - Dependency injection patterns for testability
  - Secure credential handling

## How to use

```bash
uvx copier copy --trust git@github.com:joejoinerr/python-template.git <your-directory>
```

This will ask you some questions about your project. It will then create the
project in the directory you specified, make an initial Git commit, install
dependencies, format the code and install the pre-commit hooks.
