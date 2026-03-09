import logging
from django.shortcuts import render
from django.http import Http404
from .models import Profile

logger = logging.getLogger(__name__)


def index(request):
    """Displays a list of all user profiles."""
    logger.info("La page index des Profiles a été consultée.")
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """Displays the details of a specific user profile."""
    try:
        profile = Profile.objects.get(user__username=username)
        logger.info(f"Détail consulté pour le profil de : {username}")
        context = {'profile': profile}
        return render(request, 'profiles/profile.html', context)

    except Profile.DoesNotExist as e:
        logger.error(f"Erreur : Le profil de {username} n'existe pas. ({e})")
        raise Http404("Profil introuvable")
