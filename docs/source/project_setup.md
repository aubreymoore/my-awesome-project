---
title: Project Setup
author: "Aubrey Moore"
date: "2026-03-16"
# geometry: "a4paper, margin=1.5cm"
# documentclass: article
# fontsize: 12pt
# urlcolor: blue
# toc: true
exports: ["pdf"]
---
<!--
# My Original Prompt
Please provide detailed instructions in markdown format for setting up a python project which uses 
- sphinx with myst-parser and autoapi for documentation
- github and read-the-docs for rendering documentation
- use uv for building a virtual environment and for adding packages and tools

# Gemini's Response

Setting up a modern Python project with `uv` and automated documentation is a great move. `uv` is significantly faster than traditional tools, and `myst-parser` allows you to write your docs in Markdown rather than reStructuredText.

Here is your step-by-step guide to getting this ecosystem running.

---

## 1. Project Initialization with `uv`

First, ensure you have `uv` installed. Then, create your project structure.

```bash
# Create a new project
uv init my-awesome-project
cd my-awesome-project

# Create the virtual environment and lockfile
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

```

## 2. Install Dependencies

You need Sphinx, the MyST parser (for Markdown support), and AutoAPI (to generate docs from docstrings without manual imports).

```bash
# Add documentation tools as development dependencies
uv add --dev sphinx myst-parser sphinx-autoapi sphinx-rtd-theme

```

---

## 3. Initialize Sphinx

Create a `docs` directory and set up the basic Sphinx configuration.

```bash
mkdir docs
cd docs
uv run sphinx-quickstart

```

* **Separate source and build directories?** Yes
* **Project name/Author:** Your choice

### Configure `conf.py`

Open `docs/source/conf.py` and modify the extensions and theme:

```python
import os
import sys
from datetime import date

# Basic info
project = 'My Awesome Project'
copyright = f'{date.today().year}, Your Name'
author = 'Your Name'

# -- General configuration ---------------------------------------------------
extensions = [
    'myst_parser',
    'sphinx_autoapi.extension',
    'sphinx.ext.napoleon', # Supports Google/NumPy docstrings
    'sphinx.ext.viewcode',  # Adds links to highlighted source code
]

# AutoAPI settings
autoapi_dirs = ['../../src'] # Point to your source code
autoapi_type = 'python'

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'

```

---

## 4. Connect to GitHub

1. Initialize git: `git init`
2. Create a `.gitignore` file (include `.venv/`, `build/`, and `__pycache__/`).
3. Commit your code and push it to a new GitHub repository.

---

## 5. Configure Read the Docs (RTD)

Read the Docs requires a configuration file in your project root to know how to build your environment using `uv`.

Create a file named `.readthedocs.yaml` in your **project root**:

```yaml
version: 2

build:
  os: ubuntu-22.04
  tools:
    python: "3.12"
  jobs:
    post_install:
      # Install uv
      - curl -LsSf https://astral.sh/uv/install.sh | sh
      - export PATH="$HOME/.cargo/bin:$PATH"
      # Use uv to install dependencies into the RTD environment
      - uv pip install .[dev] --system

sphinx:
  configuration: docs/source/conf.py

python:
  install:
    - method: pip
      path: .
      extra_requirements:
        - dev

```

> **Note:** Ensure your `pyproject.toml` has a `[project.optional-dependencies]` section named `dev` that includes your sphinx packages so the command `uv pip install .[dev]` works correctly.

### Finalizing on RTD Dashboard:

1. Log in to [Read the Docs](https://readthedocs.org/).
2. Import your GitHub repository.
3. RTD will detect the `.readthedocs.yaml` and trigger the build automatically.

---

### Project Structure Overview

Your final structure should look like this:

* `src/`: Your Python packages.
* `docs/source/`: Sphinx config and `.md` files.
* `pyproject.toml`: Managed by `uv`.
* `.readthedocs.yaml`: Build instructions for the cloud.

---

Would you like me to generate a starter `pyproject.toml` file that includes the necessary metadata and dependency groups for this setup?

Yes

Here is a complete, production-ready `pyproject.toml` file. This configuration uses the modern **dynamic** versioning style and organizes your documentation tools into an optional dependency group, which makes the Read the Docs build much cleaner.

### The `pyproject.toml` Template

```toml
[project]
name = "my-awesome-project"
version = "0.1.0"
description = "A short description of my project"
readme = "README.md"
requires-python = ">=3.9"
authors = [
    { name = "Your Name", email = "your.email@example.com" }
]
dependencies = [
    # Add your runtime dependencies here (e.g., "requests>=2.31.0")
]

[project.optional-dependencies]
dev = [
    "sphinx>=7.0.0",
    "myst-parser>=2.0.0",
    "sphinx-autoapi>=3.0.0",
    "sphinx-rtd-theme>=2.0.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.uv]
dev-dependencies = [
    "pytest>=8.0.0",
]

```

---

### Understanding the Directory Structure

Before you push to GitHub, ensure your folder structure looks like the diagram below. This layout ensures `autoapi` can easily find your source code and `uv` can install the package in editable mode.

### Why this setup works:

1. **`src` Layout:** By putting your code in `src/my_package`, you prevent Sphinx from accidentally importing the local folder instead of the installed package, which avoids common "ModuleNotFound" errors on Read the Docs.
2. **Optional Dependencies:** By putting Sphinx in `[project.optional-dependencies]`, you can run `uv pip install ".[dev]"` on any machine (or CI/CD server) to get the exact environment needed to build the docs.
3. **AutoAPI vs. Autodoc:** Unlike standard `autodoc`, `autoapi` doesn't need to "import" your code to document it—it maps the syntax tree. This means you don't run into issues with complex C-dependencies during the doc build.

---

### Final Verification Step

To make sure everything is wired correctly before pushing to GitHub, run this command in your terminal:

```bash
# Build the docs locally to test
uv run sphinx-build -b html docs/source docs/build

```

If that command finishes without errors, your documentation will be available locally at `docs/build/index.html` and is ready for Read the Docs.

**Would you like me to provide a starter `index.md` file with the specific MyST syntax for a Table of Contents?**
-->

# Project Setup: Sphinx, MyST, AutoAPI, and uv

This document, created with [help from Gemini](https://gemini.google.com/share/7b87f0c8737a), provides a comprehensive guide to setting up a modern Python project using `uv` for package management and `Sphinx` with `MyST-Parser` for Markdown-based documentation.

---

## 1. Project Structure

Following the modern "src-layout" is recommended for Python projects to ensure that tests and documentation tools interact with the installed package rather than local folders.

```text
my-awesome-project/
├── .github/
│   └── workflows/          # GitHub Actions (Optional)
├── docs/
│   ├── build/              # Generated documentation (git-ignored)
│   └── source/
│       ├── conf.py         # Sphinx configuration
│       └── index.md        # Documentation entry point
├── src/
│   └── my_package/         # Your actual Python code
│       ├── __init__.py
│       └── core.py
├── .gitignore
├── .readthedocs.yaml       # Read the Docs configuration
├── pyproject.toml          # Project metadata and dependencies
└── README.md
```

---

## 2. Initializing the Project with `uv`

First, initialize your project and virtual environment. `uv` is significantly faster than `pip` and manages environments automatically.

```bash
# Initialize a new project
uv init my-awesome-project
cd my-awesome-project

# Create and activate the virtual environment
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

```

---

## 3. The `pyproject.toml` Configuration

Update your `pyproject.toml` to include the documentation tools in an optional dependency group. This allows Read the Docs to install only what is necessary for the build.

```toml
[project]
name = "my-awesome-project"
version = "0.1.0"
description = "A modern Python project with Markdown docs"
readme = "README.md"
requires-python = ">=3.13"
authors = [
    { name = "Your Name", email = "your.email@example.com" }
]
dependencies = []

[project.optional-dependencies]
docs = [
    "sphinx>=9.1.0",
    "myst-parser>=5.0.0",
    "sphinx-autoapi>=3.8.0",
    "sphinx-rtd-theme>=2.0.0",
]

<!-- [build-system]
requires = ["hatchling"]
build-backend = "hatchling.build" -->
```

Install the documentation dependencies locally:

```bash
uv pip install -e ".[docs]"
```

---

## 4. Sphinx and AutoAPI Configuration

Create a `docs` directory and set up the basic Sphinx configuration.

```bash
mkdir docs
cd docs

# the following command opens a dialog
# respond as follows

# > Separate source and build directories (y/n) [n]: y
# > Project name: My Awesome Project
# > Author name(s): Aubrey Moore
# > Project release []: 0.0.1
# > Project language [en]: 

uv run sphinx-quickstart
```

Inside `docs/source/conf.py`, configure the extensions to support Markdown and automatic API generation.

```python
import os
import sys
from datetime import date

# -- Project information -----------------------------------------------------
project = 'My Awesome Project'
copyright = f'{date.today().year}, Your Name'
author = 'Your Name'

# -- General configuration ---------------------------------------------------
extensions = [
    'myst_parser',
    'sphinx_autoapi.extension',
    'sphinx.ext.napoleon',    # Support for Google/NumPy docstrings
    'sphinx.ext.viewcode',   # Links to source code
]

# AutoAPI settings: point to your src directory
autoapi_dirs = ['../../src']
autoapi_type = 'python'

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'

```

### The `index.md` File

Create `docs/source/index.md` using MyST syntax:

```markdown
# Welcome to My Awesome Project

## Introduction

This project uses `uv` for lightning-fast environment management and `MyST` for Markdown docs.
---

.. toctree ::
    :maxdepth: 2
    :caption: Contents:

    autoapi/index
```

## 5. Read the Docs Configuration

Create a `.readthedocs.yaml` file in the **root directory**. This script tells Read the Docs how to install `uv` and build your documentation.

```yaml
version: 2

build:
  os: ubuntu-24.04
  tools:
    python: "3.13"
  jobs:
    post_install:
      # Install uv
      - curl -LsSf [https://astral.sh/uv/install.sh](https://astral.sh/uv/install.sh) | sh
      - export PATH="$HOME/.cargo/bin:$PATH"
      # Install the project and doc dependencies using uv
      - uv pip install .[docs] --system

sphinx:
  configuration: docs/source/conf.py
```

---

## 6. Deployment Workflow

1. **Push to GitHub:** Initialize a git repo and push your code.
2. **Connect Read the Docs:**
* Log in to [Read the Docs](https://readthedocs.org/).
* Click **Import a Project**.
* Select your GitHub repository.


3. **Local Testing:**
Before pushing changes, you can verify the build locally using:
```bash
uv run sphinx-build -b html docs/source docs/build
```



