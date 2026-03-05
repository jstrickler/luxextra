from django.urls import reverse
import pytest
from artworks.tate_test_data import ARTISTS_DATA, ARTWORKS_DATA

@pytest.mark.django_db
@pytest.mark.parametrize('guid,artist_name', ARTISTS_DATA)
def test_can_retrieve_artist_detail_via_guid(client, guid, artist_name):
    artist_detail_url = reverse('classviews:artistdetail', args=(guid,))
    response = client.get(artist_detail_url)
    assert response.status_code == 200
    assert artist_name in response.content.decode()


@pytest.mark.django_db
@pytest.mark.parametrize('guid,artwork_title', ARTWORKS_DATA)
def test_can_retrieve_artwork_detail_via_guid(client, guid, artwork_title):
    artwork_detail_url = reverse('classviews:artworkdetail', args=(guid,))
    response = client.get(artwork_detail_url)
    assert response.status_code == 200
    assert artwork_title in response.content.decode()
