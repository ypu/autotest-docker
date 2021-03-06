"""
Docker Autotest documentation build configuration file, created by

This file is execfile()d with the current directory set to its containing dir.

Note that not all possible configuration values are present in this
autogenerated file.

All configuration values have a default; values that are commented out
serve to show the default.
"""

# Okay to be less-strict for these
# pylint: disable=C0103,C0111,R0904,C0103,C0301,W0622

import sys
import os
import types

#: The documentation version for this instance of the test.  It is compared
#: to the API version before every test.  This ensures any API changes
#: are also reflected in documentation.
#:
#: The short X.Y version. This MUST be inside single ("'") quotes for parsing!!
version = '0.8.3'

#: If extensions (or modules to document with autodoc) are in another directory,
#: add these directories to sys.path here. If the directory is relative to the
#: documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('dockertest'))

# -- General configuration -----------------------------------------------------

#: If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.1'

#: Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.intersphinx', 'sphinx.ext.autodoc', 'sphinx.ext.viewcode']

#: Add any paths that contain templates here, relative to this directory.
templates_path = ['docs_templates']

#: The suffix of source filenames.
source_suffix = '.rst'

#: The encoding of source files.
source_encoding = 'utf-8-sig'

#: The master toctree document.
master_doc = 'index'

#: General information about the project.
project = u'Docker Autotest'
copyright = u'2014, Chris Evich'

#: The full version, including alpha/beta/rc tags.
release = '.'.join(version.split('.')[0:2])

#: The language for content autogenerated by Sphinx. Refer to documentation
#: for a list of supported languages.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

#: List of patterns, relative to source directory, that match files and
#: directories to ignore when looking for source files.
exclude_patterns = ['docs_build', 'config.d', 'README.rst', 'config_custom/README.rst']

#: The reST default role (used for this markup: `text`) to use for all documents.
default_role = None

#: If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

#: If true, the current module name will be prepended to all description
#: unit titles (such as .. function::).
add_module_names = True

#: If true, sectionauthor and moduleauthor directives will be shown in the
#: output. They are ignored by default.
show_authors = False

#: The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

#: A list of ignored prefixes for module index sorting.
modindex_common_prefix = []

#: Allow using a no- prefix with options
autodoc_default_flags = ['members', 'undoc-members', 'inherited-members',
                         'show-inheritance']

#: By default, class/module members are ordered alphabeticaly.
#: However, in this project the layout is all logically ordered
autodoc_member_order = 'bysource'

# -- Options for HTML output ---------------------------------------------------

#: The theme to use for HTML and HTML Help pages.  See the documentation for
#: a list of builtin themes.
html_theme = 'default'

#: Theme options are theme-specific and customize the look and feel of a theme
#: further.  For a list of options available for each theme, see the
#: documentation.
html_theme_options = {'stickysidebar': True}

#: Add any paths that contain custom themes here, relative to this directory.
html_theme_path = []

#: The name for this set of Sphinx documents.  If None, it defaults to
#: "<project> v<release> documentation".
html_title = "Docker Autotest Documentation"

#: A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = None

#: The name of an image file (relative to this directory) to place at the top
#: of the sidebar.
html_logo = None

#: The name of an image file (within the static path) to use as favicon of the
#: docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
#: pixels large.
html_favicon = None

#: Add any paths that contain custom static files (such as style sheets) here,
#: relative to this directory. They are copied after the builtin static files,
#: so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['docs_static']

#: If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
#: using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

#: If true, SmartyPants will be used to convert quotes and dashes to
#: typographically correct entities.
html_use_smartypants = True

#: Custom sidebar templates, maps document names to template names.
html_sidebars = {'**': ['searchbox.html', 'localtoc.html']}

#: Additional templates that should be rendered to pages, maps page names to
#: template names.
html_additional_pages = {}

#: If false, no module index is generated.
html_domain_indices = True

#: If false, no index is generated.
html_use_index = True

#: If true, the index is split into individual pages for each letter.
html_split_index = False

#: If true, links to the reST sources are added to the pages.
html_show_sourcelink = True

#: If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = True

#: If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

#: If true, an OpenSearch description file will be output, and all pages will
#: contain a <link> tag referring to it.  The value of this option must be the
#: base URL from which the finished HTML is served.
html_use_opensearch = ''

#: This is the file name suffix for HTML files (e.g. ".xhtml").
html_file_suffix = None

#: Output file base name for HTML help builder.
htmlhelp_basename = 'DockerAutotestdoc'


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
}

#: Grouping the document tree into LaTeX files. List of tuples
#: (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ('index', 'DockerAutotest.tex', u'Docker Autotest Documentation',
     u'Chris Evich', 'manual'),
]

#: The name of an image file (relative to this directory) to place at the top of
#: the title page.
latex_logo = None

#: For "manual" documents, if this is true, then toplevel headings are parts,
#: not chapters.
latex_use_parts = False

#: If true, show page references after internal links.
latex_show_pagerefs = False

#: If true, show URL addresses after external links.
latex_show_urls = False

#: Documents to append as an appendix to all manuals.
latex_appendices = []

#: If false, no module index is generated.
latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

#: One entry per manual page. List of tuples
#: (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'dockerautotest', u'Docker Autotest Documentation',
     [u'Chris Evich'], 1)
]

#: If true, show URL addresses after external links.
man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

#: Grouping the document tree into Texinfo files. List of tuples
#: (source start file, target name, title, author,
#: dir menu entry, description, category)
texinfo_documents = [
    ('index', 'DockerAutotest', u'Docker Autotest Documentation',
     u'Chris Evich', 'DockerAutotest', 'One line description of project.',
     'Miscellaneous'),
]

#: Documents to append as an appendix to all manuals.
texinfo_appendices = []

#: If false, no module index is generated.
texinfo_domain_indices = True

#: How to display URL addresses: 'footnote', 'no', or 'inline'.
texinfo_show_urls = 'footnote'


# -- Module mocking so we don't hang up on external dependencies ---------------

# DO NOT allow this function to get loose in the wild!
def mock(mod_path):
    """
    Recursivly inject tree of mocked modules from entire mod_path
    """
    name_list = mod_path.split('.')
    child_name = name_list.pop()
    child_mod = sys.modules.get(mod_path, types.ModuleType(child_name))
    if len(name_list) == 0:  # child_name is left-most basic module
        if not sys.modules.has_key(child_name):
            sys.modules[child_name] = child_mod
        return sys.modules[child_name]
    else:
        # New or existing child becomes parent
        recurse_path = ".".join(name_list)
        parent_mod = mock(recurse_path)
        if not hasattr(sys.modules[recurse_path], child_name):
            setattr(parent_mod, child_name, child_mod)
            # full-name also points at child module
            sys.modules[mod_path] = child_mod
        return sys.modules[mod_path]

mock('autotest.client.shared')
setattr(mock('autotest.client.utils'), 'CmdResult', type)
setattr(mock('autotest.client.utils'), 'run', object)
setattr(mock('autotest.client.utils'), 'AsyncJob', object)
setattr(mock('autotest.client.utils'), 'wait_for', object)
setattr(mock('autotest.client.shared'), 'service', object)
# Mock module and test class in one call
setattr(mock('autotest.client.test'), 'test', type)
setattr(mock('autotest.client.shared.error'), 'CmdError', Exception)
setattr(mock('autotest.client.shared.error'), 'TestFail', Exception)
setattr(mock('autotest.client.shared.error'), 'TestError', Exception)
setattr(mock('autotest.client.shared.error'), 'TestNAError', Exception)
setattr(mock('autotest.client.shared.error'), 'AutotestError', Exception)
setattr(mock('autotest.client.shared.version'), 'get_version', lambda: "0.15.0")
mock('autotest.client.shared.base_job')
mock('autotest.client.shared.utils')
mock('autotest.client.shared.job')
mock('autotest.client.job')

# -- Build subtests.rst, additional.rst, and defaults.rst ---------------

from dockertest.documentation import DefaultDoc
from dockertest.documentation import SubtestDocs
from dockertest.documentation import PretestDoc
from dockertest.documentation import IntratestDoc
from dockertest.documentation import PosttestDoc
open('defaults.rst', 'w+').write(str(DefaultDoc('config_defaults/defaults.ini')))
open('subtests.rst', 'w+').write(str(SubtestDocs()))
additional = open('additional.rst', 'w+')
# Only include contents block once for all three types
include_contents = True
for cls in (PretestDoc, IntratestDoc, PosttestDoc):
    additional.write(str(SubtestDocs(subtestdocclass=cls,
                                     contents=include_contents)))
    additional.write('\n\n')
    if include_contents:
        include_contents = False
