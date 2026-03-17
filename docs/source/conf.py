# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from datetime import date

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'My Awesome Project'
copyright = f'{date.today().year}, Aubrey Moore'
author = 'Aubrey Moore'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'autoapi.extension',
    'sphinx.ext.napoleon',    # Support for Google/NumPy docstrings
    'sphinx.ext.viewcode',   # Links to source code
]

# AutoAPI settings: point to your src directory
autoapi_dirs = ['../../src']
autoapi_type = 'python'

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_context = {
    "display_github": True,  # Integrate GitHub
    "github_user": "aubreymoore",  # Username
    "github_repo": "my-awesome-project",  # Repo name
    "github_version": "main",  # Version/branch name
    "conf_py_path": "/docs/source/",  # Path in the checkout to the docs root (adjust as needed)
}

