"""
Views for the main application oc_lettings_site.
This module contains the view for the home page.
"""
from django.shortcuts import render
import logging


logger = logging.getLogger(__name__)


def index(request):
    """Displays the home page of the application."""
    logger.info("La page d'accueil principale a été consultée.")
    return render(request, 'index.html')
