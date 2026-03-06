from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile


def test_profile_model_str(db):
    """Tests the string representation of Profile."""
    user = User.objects.create(username="johndoe")
    profile = Profile.objects.create(user=user, favorite_city="Paris")

    assert str(profile) == "johndoe"


def test_profiles_index_view(client, db):
    """Tests if the profiles index page loads correctly."""
    url = reverse('profiles:index')
    response = client.get(url)

    assert response.status_code == 200
    assert b"<title>Profiles</title>" in response.content


def test_profile_detail_view(client, db):
    """Tests if a specific profile page loads correctly."""
    user = User.objects.create(username="johndoe")
    Profile.objects.create(user=user, favorite_city="Paris")
    url = reverse('profiles:profile', args=["johndoe"])

    response = client.get(url)
    assert response.status_code == 200
    assert b"johndoe" in response.content
