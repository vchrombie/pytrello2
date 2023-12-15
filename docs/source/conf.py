# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

from typing import Any

sys.path.insert(0, os.path.abspath(".."))

project = "pytrello2"
copyright = "2023, pytrello2 maintainers"
author = "pytrello2 maintainers"
release = "0.1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx.ext.autodoc",
    "sphinx_copybutton",
    "myst_parser",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", ".DS_Store", "README.md"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
# html_static_path = ["_static"]
html_logo = "../../assets/pytrello2.png"
html_favicon = "../../assets/pytrello2.png"
html_css_files: Any = [
    "css/custom.css",
]
html_theme_options = {"style_nav_header_background": "#011d41"}
html_context: Any = {
    "display_github": True,
    "github_user": "pytrello2",
    "github_repo": "pytrello2",
    "github_version": "master/docs/source/",
}
