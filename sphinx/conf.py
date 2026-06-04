import os
import sys
from importlib.metadata import version as get_version

sys.path.insert(0, os.path.abspath("../src"))

project = "elizur"
copyright = "2019, Tanner Rollefson"
author = "Tanner Rollefson"

_version = get_version("elizur")
version = _version
release = _version

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
]

templates_path = ["_templates"]
exclude_patterns = []

html_title = f"{project} {version} Documentation"
html_logo = "elizur_avatar.png"
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "display_version": True,
    "style_nav_header_background": "#520707",
    "collapse_navigation": False,
}
html_static_path = ["_static"]

intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}
