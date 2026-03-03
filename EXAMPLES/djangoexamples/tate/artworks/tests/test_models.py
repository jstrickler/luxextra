from time import sleep
from django.urls import reverse
import pytest
from artworks.models import Artist, Artwork
from artworks.tate_test_data import ARTISTS_DATA, ARTWORKS_DATA

@pytest.mark.django_db
@pytest.mark.parametrize('guid,artist_name', ARTISTS_DATA)
def test_can_get_artist_name_via_guid(client, db, guid, artist_name):
    artist = Artist.objects.get(pk=guid)
    assert artist.name == artist_name


@pytest.mark.django_db
@pytest.mark.parametrize('guid,artwork_title', ARTWORKS_DATA)
def test_can_get_artwork_title_via_guid(guid, artwork_title):
    artwork = Artwork.objects.get(pk=guid)
    assert artwork.title == artwork_title
