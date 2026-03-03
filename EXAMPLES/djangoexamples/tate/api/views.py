from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from artworks.models import Artist, Artwork
from .serializers import ArtistSerializer, ArtworkSerializer
from .filters import ArtistFilter, ArtworkFilter

# function-based view (aka FBV)

@api_view(['GET'])
def artist(request, pk):
    """
    Function-based view to retrieve one artist.
    """
    artist = get_object_or_404(Artist, id=pk)
    serializer = ArtistSerializer(artist, context={'request': request})
    return Response(serializer.data)




# class-based views (aka CBVs)

# Responds to GET and POST requests with no PK specified
class ArtistList(ListCreateAPIView):
    model = Artist
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ArtistFilter


# Responds to GET, PUT, PATCH, and DELETE requests with PK specified
class ArtistDetail(RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ArtistFilter

# Responds to GET and POST requests with no PK specified
class ArtworkList(ListCreateAPIView):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ArtworkFilter


# Responds to GET, PUT, PATCH, and DELETE requests with PK specified
class ArtworkDetail(RetrieveUpdateDestroyAPIView):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ArtworkFilter
