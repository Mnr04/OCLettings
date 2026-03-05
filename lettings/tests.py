from django.urls import reverse
from .models import Address, Letting


def test_address_model_str(db):
    """Tests the string representation of Address."""
    address = Address.objects.create(
        number=123, street="Main St", city="Testville",
        state="TS", zip_code=12345, country_iso_code="TES"
    )
    assert str(address) == "123 Main St"

def test_letting_model_str(db):
    """Tests the string representation of Letting."""
    address = Address.objects.create(
        number=123, street="Main St", city="Testville",
        state="TS", zip_code=12345, country_iso_code="TES"
    )
    letting = Letting.objects.create(title="Super Appart", address=address)
    assert str(letting) == "Super Appart"

def test_lettings_index_view(client):
    """Tests if the index page loads correctly."""
    url = reverse('lettings:index')
    response = client.get(url)
    assert response.status_code == 200
    assert b"<title>Lettings</title>" in response.content

def test_letting_detail_view(client, db):
    """Tests if a specific letting page loads correctly."""
    address = Address.objects.create(
        number=123, street="Main St", city="Testville",
        state="TS", zip_code=12345, country_iso_code="TES"
    )
    letting = Letting.objects.create(title="Super Appart", address=address)
    url = reverse('lettings:letting', args=[letting.id])

    response = client.get(url)
    assert response.status_code == 200
    assert b"Super Appart" in response.content