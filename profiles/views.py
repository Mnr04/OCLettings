from .models import Profile
from django.shortcuts import render


def index(request):
    """Displays a list of all user profiles."""
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """Displays the details of a specific user profile."""
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
