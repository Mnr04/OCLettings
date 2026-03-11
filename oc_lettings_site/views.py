"""
Views for the main application oc_lettings_site.
This module contains the view for the home page.
"""
from django.shortcuts import render


def index(request):
    """Displays the home page of the application."""
    return render(request, 'index.html')
