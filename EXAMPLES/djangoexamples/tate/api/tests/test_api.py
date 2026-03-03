from django.urls import reverse
from rest_framework.test import APIClient
import pytest
from artworks.models import Artist, Artwork
from artworks.tate_test_data import ARTISTS_DATA, ARTWORKS_DATA

PREFIX = "http://127.0.0.1:8000"

@pytest.mark.django_db
@pytest.mark.parametrize('guid,artist_name', ARTISTS_DATA)
def test_artist_guid_retrieves_correct_name(client, guid, artist_name):
    artist_url = reverse('api:artists-detail', args=(guid,))
    response = client.get(artist_url)
    assert response.data["name"] == artist_name

@pytest.mark.django_db
@pytest.mark.parametrize('guid,artwork_title', ARTWORKS_DATA)
def test_artwork_guid_retrieves_correct_title(client, guid, artwork_title):
    artwork_url = reverse('api:artworks-detail', args=(guid,))
    response = client.get(artwork_url)        
    assert response.data['title'] == artwork_title

