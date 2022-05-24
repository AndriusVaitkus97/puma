# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys

sys.path.insert(0, os.path.abspath("../../puma"))


# -- Project information -----------------------------------------------------

project = "puma"
copyright = "2022, puma developers"
author = "puma developers"

# The full version, including alpha/beta/rc tags
release = ""


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "myst_parser",
    "sphinx.ext.napoleon",
    "autoapi.extension",
    "sphinx_multiversion",
]

# Configuration of sphinx-autoapi extension
# https://sphinx-autoapi.readthedocs.io/en/latest/reference/config.html#
autoapi_type = "python"
autoapi_dirs = ["../../puma"]
autoapi_python_use_implicit_namespaces = True
autoapi_python_class_content = "both"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]
html_sidebars = {
    "**": [
        "versioning.html",
    ],
}

# -- sphinx-multiversion settings -------------------------------------------
# define which tags are used in sphinx-multiversion
smv_tag_whitelist = r"^v\d+\.\d+\.\d+$"  # only tags of the form vX.X.X
# define which branches are used in sphinx-multiversion
smv_branch_whitelist = r"(main)$"  # only use main branch
smv_remote_whitelist = r"(main)$"  # only use origin/main branch

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
html_static_path = ["_static"]

default_role = "code"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# TODO: define url of the json dict that stores the different docs version links
# json_url = "https://umami-hep.github.io/puma/main/_static/switcher.json"

html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/umami-hep/puma",
            "icon": "fab fa-github-square",
            "type": "fontawesome",
        },
    ],
    # TODO: implement this
    # "switcher": {
    #     "json_url": json_url,
    #     "version_match": "latest",
    # },
    # "navbar_end": ["version-switcher", "navbar-icon-links"]
}

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "friendly"
