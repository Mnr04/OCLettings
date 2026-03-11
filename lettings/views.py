"""
Views for the lettings application.
"""
import logging
from django.shortcuts import render
from django.http import Http404
from .models import Letting

logger = logging.getLogger(__name__)


def index(request):
    """Displays a list of all lettings."""
    logger.info("La page index des Lettings a été consultée.")
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """Displays the details of a specific letting based on its ID."""
    try:
        letting = Letting.objects.get(id=letting_id)
        logger.info(f"Détail consulté pour la location: {letting.title}")
        context = {
            'title': letting.title,
            'address': letting.address,
        }
        return render(request, 'lettings/letting.html', context)

    except Letting.DoesNotExist as e:
        logger.error(f"Erreur: La location avec l'ID {letting_id} n'existe pas. ({e})")
        raise Http404("Location introuvable")
