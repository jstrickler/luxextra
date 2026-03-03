#from django.http import HttpResponse # only used in class (see comment below)
from typing import Any
from django.views.generic import DetailView, ListView
from django_filters.views import  FilterView
from django.shortcuts import render
from artworks.models import Artist, Artwork
from api.filters import ArtistFilter, ArtworkFilter
from artworks.forms import ArtistSearchForm

# Create your views here.

# example without template
# def home(request):
#     return HttpResponse("Welcome to Tate classviews")

# example with template (normal Django approach)
def home(request):
    artist = Artist.objects.order_by('name').first()
    artwork = Artwork.objects.order_by('title').first()
    context = { 
        'message': "Welcome to Tate Class-based Views",
        'artist': artist,
        'artwork': artwork,
    }
    return render(request, 'classviews/home.html', context)

class ArtistFilterView(FilterView): # FKA ArtistListView
    model = Artist
    paginate_by = 25
    filterset_class = ArtistFilter
#    template_name = 'artworks/artist_list.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context_data = super().get_context_data(**kwargs)
        context_data['artist_search_form'] = ArtistSearchForm()
        return context_data

    def get_queryset(self):
        query_set = super().get_queryset()
        order_by_field = self.request.GET.get('order_by', 'name')
        query_set = query_set.order_by(order_by_field)
        return query_set

class ArtworkFilterView(FilterView):
    model = Artwork
    paginate_by = 20
    filterset_class = ArtworkFilter
#    template_name = 'artworks/artwork_list.html'

    def get_queryset(self):
        query_set = super().get_queryset()
        order_by_field = self.request.GET.get('order_by', 'title')
        query_set = query_set.order_by(order_by_field)
        return query_set

class ArtistDetailView(DetailView):
    model = Artist

class ArtworkDetailView(DetailView):
    model = Artwork