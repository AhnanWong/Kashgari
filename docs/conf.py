#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest.mock import MagicMock
import os
import sys

# Make sure spinup is accessible without going through setup.py
dirname = os.path.dirname
sys.path.insert(0, dirname(dirname(__file__)))

import kashgari
# Mock mpi4py to get around having to install it on RTD server (which fails)
# Also to mock PyTorch, because it is too large for the RTD server to download


class Mock(MagicMock):
    @classmethod
    def __getattr__(cls, name):
        return MagicMock()


MOCK_MODULES = [
    # 'keras.layers',
    # 'tensorflow',
    # 'tensorflow.keras',
    # 'tensorflow.keras.utils',
    # 'tensorflow.keras.preprocessing.sequence',
    # 'tensorflow.keras.callbacks',
    # 'tensorflow.keras.backend',
    # 'tensorflow.keras.layers',
    # 'tensorflow.python',
    # 'tensorflow.python.util',
    # 'tensorflow.python.util.tf_export',
    # 'bert4keras',
    # 'bert4keras.models',
    # 'sklearn',
    # 'bert4keras.layers'
]

sys.modules.update((mod_name, Mock()) for mod_name in MOCK_MODULES)


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'recommonmark',
    'sphinx_markdown_tables',
    'sphinx.ext.imgmath',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx_autodoc_typehints'
]

# sphinx_autodoc_typehints settings
autodoc_default_options = {
    'member-order': 'groupwise',
    'special-members': '__init__',
    'undoc-members': False,
    'inherited-members': True,
    'show-inheritance': True,
    'set_type_checking_flag': True
}

# 'sphinx.ext.mathjax', ??

# imgmath settings
imgmath_image_format = 'svg'
imgmath_font_size = 14

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
# source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Kashgari'
copyright = '2019, BrikerMan'
author = 'Eliyar Eziz'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = kashgari.__version__
# The full version, including alpha/beta/rc tags.
release = kashgari.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'default'  # 'sphinx'

todo_include_todos = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# html_logo = 'images/logo.png'
# html_theme_options = {
#     'logo_only': True
# }
# html_favicon = 'openai-favicon2_32x32.ico'
# html_favicon = 'openai_icon.ico'

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'KashgariDoc'

# -- Options for LaTeX output ---------------------------------------------


imgmath_latex_preamble = r'''
\usepackage{algorithm}
\usepackage{algorithmic}
\usepackage{amsmath}
\usepackage{cancel}

\usepackage[verbose=true,letterpaper]{geometry}
\geometry{
    textheight=12in,
    textwidth=6.5in,
    top=1in,
    headheight=12pt,
    headsep=25pt,
    footskip=30pt
    }

\newcommand{\E}{{\mathrm E}}

\newcommand{\underE}[2]{\underset{\begin{subarray}{c}#1 \end{subarray}}{\E}\left[ #2 \right]}

\newcommand{\Epi}[1]{\underset{\begin{subarray}{c}\tau \sim \pi \end{subarray}}{\E}\left[ #1 \right]}
'''

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    'preamble': r'''
\usepackage{algorithm}
\usepackage{algorithmic}
\usepackage{amsmath}
\usepackage{cancel}


\newcommand{\E}{{\mathrm E}}

\newcommand{\underE}[2]{\underset{\begin{subarray}{c}#1 \end{subarray}}{\E}\left[ #2 \right]}

\newcommand{\Epi}[1]{\underset{\begin{subarray}{c}\tau \sim \pi \end{subarray}}{\E}\left[ #1 \right]}
''',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'Kashgari.tex', 'Kashgari Documentation',
     'Eliyar Eziz', 'manual'),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'kashgari', 'Kashgari Documentation',
     [author], 1)
]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Kashgari', 'Kashgari Documentation',
     author, 'Kashgari', 'One line description of project.',
     'Miscellaneous'),
]


def update_markdown_content(folder: str):
    import os
    import glob
    from m2r import convert
    files = []

    for file in glob.glob(os.path.join(folder, "*.md")):
        files.append(file)
    for file in glob.glob(os.path.join(folder, "*/*.md")):
        files.append(file)
    for file in glob.glob(os.path.join(folder, "*/*/*.md")):
        files.append(file)

    for file in files:
        print(f"update markdown file: {file}")
        with open(file, 'r') as original:
            content = original.read()
        with open(file, 'w') as new:
            new_content = content.replace('.md)', '.html)')
            new.write(new_content)


def skip_some_classes_members(app, what, name, obj, skip, options):
    return skip


# from sphinx.ext.autodoc import ClassDocumenter, _
#
# add_line = ClassDocumenter.add_line
# line_to_delete = _(u'Bases: %s') % u':class:`object`'
#
#
# def add_line_no_object_base(self, text, *args, **kwargs):
#     if text.strip() == line_to_delete:
#         return
#
#     add_line(self, text, *args, **kwargs)
#
#
# add_directive_header = ClassDocumenter.add_directive_header
#
#
# def add_directive_header_no_object_base(self, *args, **kwargs):
#     self.add_line = add_line_no_object_base.__get__(self)
#
#     result = add_directive_header(self, *args, **kwargs)
#
#     del self.add_line
#
#     return result


# ClassDocumenter.add_directive_header = add_directive_header_no_object_base


intersphinx_mapping = {
    'python': ('https://docs.python.org/', None),
    'sqlalchemy': ('http://docs.sqlalchemy.org/en/latest/', None),
    'tensorflow': ('https://www.tensorflow.org/versions/r2.2/api_docs/', None)
    }


def setup(app):
    import pathlib

    from m2r import convert
    import typing
    import shutil

    typing.TYPE_CHECKING = True

    docs_path = pathlib.Path(__file__).parent
    original_readme = os.path.join(docs_path.parent, 'README.md')
    rst_readme = os.path.join(docs_path, 'README.rst')

    # Copy Examples to docs folder for rendering
    original_examples_folder = os.path.join(docs_path.parent, 'examples')
    target_examples_folder = os.path.join(docs_path, 'examples')
    shutil.rmtree(target_examples_folder, ignore_errors=True)

    shutil.copytree(original_examples_folder,
                    target_examples_folder,
                    symlinks=True)

    # Change readme to rst file, and include in Sphinx index
    with open(rst_readme, 'w') as f:
        md_content = open(original_readme, 'r').read()
        md_content = md_content.replace('(./docs/', '(./')
        md_content = md_content.replace('(./examples/',
                                        '(https://github.com/BrikerMan/Kashgari/blob/v2-trunk/examples/')
        md_content = md_content.replace('.md)', '.html)')
        f.write(convert(md_content))
        print(f'Saved RST file to {rst_readme}')

    # Update all .md files， for fixing links
    update_markdown_content(docs_path)

    app.add_css_file('css/modify.css')
    app.add_css_file('css/extra.css')

    app.config['set_type_checking_flag'] = True
    app.config['autodoc_mock_imports'] = MOCK_MODULES
    app.connect('autodoc-skip-member', skip_some_classes_members)
