from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework_api_key.models import APIKey
import pytest
from artworks.tate_test_data import ARTISTS_DATA, ARTWORKS_DATA

@pytest.fixture
def api_client():
    client = APIClient()
    _, key = APIKey.objects.create_key(name="test-key")
    print(f"{key = }")
    
    client.credentials(HTTP_AUTHORIZATION=f"api-key {key}")
    return client

@pytest.mark.django_db
@pytest.mark.parametrize('guid,artist_name', ARTISTS_DATA)
def test_artist_guid_retrieves_correct_name(api_client, guid, artist_name):
    artist_url = reverse('api:artists-detail', args=(guid,))
    response = api_client.get(artist_url)
    assert response.data["name"] == artist_name

@pytest.mark.django_db
@pytest.mark.parametrize('guid,artwork_title', ARTWORKS_DATA)
def test_artwork_guid_retrieves_correct_title(api_client, guid, artwork_title):
    artwork_url = reverse('api:artworks-detail', args=(guid,))
    response = api_client.get(artwork_url)        
    assert response.data['title'] == artwork_title

