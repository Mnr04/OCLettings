from django.shortcuts import render
from lettings.models import Letting
from profiles.models import Profile



def index(request):
    return render(request, 'index.html')

