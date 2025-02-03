# pylint: disable=invalid-name,redefined-builtin
"""
Configuration file for the Sphinx documentation builder.

For the full list of built-in configuration values, see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html

-- Project information -----------------------------------------------------
https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

-- General configuration ---------------------------------------------------
https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
"""
import sys
from pathlib import Path
import version_query


def get_release():
    """Query the current release for the project."""
    try:
        repo_path = Path(".")
        ret_value = version_query.git_query.query_git_repo(repo_path).to_str()
    except ValueError:
        ret_value = version_query.Version.from_str("0.0.1").to_str()
    return ret_value


author = "Xander Harris"
autoyaml_root = "."
autoyaml_doc_delimiter = "###"
autoyaml_comment = "#"
autoyaml_level = 10
autoyaml_safe_loader = True
copyright = "2025, Xander Harris"
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    ".pytest_cache/*",
    ".tox/*",
    ".venv/*",
]
extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_last_updated_by_git",
    "sphinx_git",
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.duration",
    "sphinx.ext.githubpages",
    "sphinx.ext.graphviz",
    "sphinx.ext.todo",
    "sphinxcontrib.autoyaml",
]
git_untracked_check_dependencies = False
graphviz_output_format = "png"
# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_context = {"full_path": str(Path(".").resolve())}
html_static_path = ["_static"]
html_theme = "sphinx_book_theme"
myst_enable_extensions = [
    "amsmath",
    "attrs_block",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]
myst_footnote_transition = True
myst_title_to_header = True
project = "Pre-Commit JIRA Ticket and GitHub Issue"
with Path(".version").open("r", encoding="utf-8") as r_fh:
    release = r_fh.read()
show_authors = True
source_suffix = {
    ".md": "markdown",
}
templates_path = ["_templates"]
