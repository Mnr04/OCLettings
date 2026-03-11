"""
Tests for the lettings application.
"""
from django.urls import reverse
from .models import Address, Letting


def test_lettings_index(client, db):
    """Test All locations"""

    address = Address.objects.create(
        number=123,
        street="Rue de la Paix",
        city="Paris",
        state="ID",
        zip_code=75000,
        country_iso_code="FRA"
    )
    Letting.objects.create(title="Appartement Test", address=address)

    url = reverse('lettings:index')
    response = client.get(url)

    assert response.status_code == 200
    assert b"Appartement Test" in response.content


def test_letting_detail(client, db):
    """Test specific locations"""

    address = Address.objects.create(
        number=45,
        street="Avenue des Champs",
        city="Paris",
        state="ID",
        zip_code=75008,
        country_iso_code="FRA"
    )
    letting = Letting.objects.create(title="Studio Chic", address=address)

    url = reverse('lettings:letting', args=[letting.id])
    response = client.get(url)

    assert response.status_code == 200
    assert b"Studio Chic" in response.content
