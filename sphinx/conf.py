# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

import elizur


def no_wrap(f):
    return f


elizur.validate_age = no_wrap
elizur.validate_age_and_interval = no_wrap

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath("../elizur"))


# -- Project information -----------------------------------------------------

project = "elizur"
copyright = "2019, Tanner Rollefson"
author = "Tanner Rollefson"

version = elizur.VERSION
release = elizur.VERSION


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named "sphinx.ext.*") or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_title = f"{project} {version} Documentation"
html_logo = "elizur_avatar.png"
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "display_version": True,
    "style_nav_header_background": "#520707",
    "collapse_navigation": False,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Intersphinx configuration
intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}
