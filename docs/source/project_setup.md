---
title: Project Setup Guide
author: "Aubrey Moore"
date: "2026-03-17"
# geometry: "a4paper, margin=1.5cm"
# documentclass: article
# fontsize: 12pt
# urlcolor: blue
# toc: true
exports: ["pdf"]
---

# Project Setup Guide

This document, created with [help from Gemini](https://gemini.google.com/share/7b87f0c8737a), provides a comprehensive guide to setting up a modern Python project which uses

- `uv` for lightning-fast environment management
- `MyST Markdown` for writing nicely formatted guides
- `Sphinx` for documenting `Python` code
- `GitHub` and `Read the Docs` for publishing

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

```{literalinclude} ../../pyproject.toml
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
# > Project name: My Awesome ProjectP
# > Author name(s): Aubrey Moore
# > Project release []: 0.0.1
# > Project language [en]: 

uv run sphinx-quickstart
```

Inside `docs/source/conf.py`, configure the extensions to support Markdown and automatic API generation.


```{literalinclude} conf.py
```

### The `index.md` File

Create `docs/source/index.md` using MyST syntax:

```{literalinclude} index.md
```

## 5. Read-the-Docs Configuration

Create a `.readthedocs.yaml` file in the **root directory**. This script tells Read the Docs how to install `uv` and build your documentation.

```{literalinclude} ../../.readthedocs.yaml
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

Then point a web browser at `docs/build/index.html`
