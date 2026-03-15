import os
import sys
import django
import sphinx_rtd_theme


sys.path.insert(0, os.path.abspath('../..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'oc_lettings_site.settings'

django.setup()

project = 'OCLettings'
copyright = '2026, JR'
author = 'JR'

extensions = [
    'sphinx.ext.autodoc',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
