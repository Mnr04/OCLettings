import os
import sys
import django


sys.path.insert(0, os.path.abspath('../..'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'oc_lettings_site.settings'
os.environ.setdefault('SECRET_KEY', 'false')

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
