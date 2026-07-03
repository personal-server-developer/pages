# pages/source/conf.py

import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

project = 'My Project'
author = 'Your Name'
release = '0.1.0'

extensions = [
    'myst_parser',
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

master_doc = 'index'
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# 推奨：サイトのベース URL を明示
html_baseurl = "https://personal-server-developer.github.io/pages/"
