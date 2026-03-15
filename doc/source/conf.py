import os
import sys
import django


current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '../..'))
sys.path.insert(0, project_root)

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
