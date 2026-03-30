# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Surya Science Workshop'
copyright = '2026 SwRI-IDEA-Lab & Trillium Technologies, Inc.'
author = 'Andrés Muñoz-Jaramillo, Russell Spiewak, Mike Heyns'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",             # Allows you to use Markdown (.md) files
    "sphinx.ext.githubpages",  # Creates the .nojekyll file for GH Pages
    "sphinx_book_theme",
]

exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"

html_theme_options = {
    "repository_url": "https://github.com/spaceml-org/surya_workshop",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "path_to_docs": "docs/source",
    "home_page_in_toc": True,
    "show_toc_level": 2,
    "announcement": "Page under construction.",
    "use_sidenotes": True,
}

html_logo = "_static/surya_manual.png"
html_favicon = "_static/surya_favicon.ico"

html_static_path = ['_static']

# Add support for both .rst and .md files
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
