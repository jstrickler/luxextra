from rest_framework import serializers
from artworks.models import Artist, Artwork


class ArtworkSerializer(serializers.ModelSerializer):
    artist = serializers.HyperlinkedRelatedField(view_name='api:artists-detail', read_only=True, )

    class Meta:
        model = Artwork
        fields = ('id', 'title', 'date_text', 'thumbnail_url', 'tate_url', 'artist')


class ArtistSerializer(serializers.ModelSerializer):

    # note view_name comes from router
    artworks = serializers.HyperlinkedRelatedField(view_name="api:artworks-detail", many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ('id', 'name', 'gender', 'place_of_birth', 'birth_year', 'death_year', 'tate_url', 'artworks')
