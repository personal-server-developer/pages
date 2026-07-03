# pages/source/conf.py

import os
import sys
from datetime import datetime

# -- Path setup --------------------------------------------------------------
sys.path.insert(0, os.path.abspath('../..'))

# -- Project information -----------------------------------------------------
project = 'My Project'
author = 'Your Name'
release = '0.1.0'
copyright = f'{datetime.now().year}, {author}'

# -- General configuration ---------------------------------------------------
extensions = [
    'myst_parser',
]

# Recognize both reStructuredText and Markdown
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# Master document
master_doc = 'index'

# Templates and exclude patterns
templates_path = ['_templates']
exclude_patterns = ['_build', 'build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Base URL for the site, useful for sitemap and absolute links
html_baseurl = "https://personal-server-developer.github.io/pages/"

# Optional: hide "View page source" link if you prefer
html_show_sourcelink = False

# Reduce noise in output
html_show_sphinx = False

# If you want to tweak theme options for Read the Docs theme, add here
html_theme_options = {
    # Example options; adjust if needed
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
}

# -- Performance and build hints ---------------------------------------------
# Keep master_doc explicit and minimal to ensure incremental builds work reliably
# Avoid heavy runtime operations in conf.py to keep CI fast

# If you use extensions that generate many files, consider enabling parallel build
# via the Makefile or SPHINXOPTS: sphinx-build -j auto

# -- Internationalization ----------------------------------------------------
# Set language if your docs are primarily Japanese
# language = 'ja'

# -- End of configuration ----------------------------------------------------
