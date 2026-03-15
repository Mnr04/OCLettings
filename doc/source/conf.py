import os
import sys
import django

# Add the project root
sys.path.insert(0, os.path.abspath('../..'))

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'oc_lettings_site.settings'

# Add a fake secret key to avoid Django errors during the build
os.environ.setdefault('SECRET_KEY', 'false')

# Start Django to allow Sphinx to read our models and views
django.setup()

# Project information
project = 'OCLettings'
copyright = '2026, JR'
author = 'JR'

# Enable autodoc to read docstrings from our Python files
extensions = [
    'sphinx.ext.autodoc',
]

templates_path = ['_templates']
exclude_patterns = []

# Use the Read the Docs visual theme
html_theme = 'sphinx_rtd_theme'
