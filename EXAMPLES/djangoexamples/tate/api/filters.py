from django_filters import rest_framework as filters
from artworks.models import Artist, Artwork

class ArtistFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="search_name", lookup_expr='icontains')
    
    birthplace = filters.CharFilter(field_name="place_of_birth", lookup_expr='icontains')
    
    deathplace = filters.CharFilter(field_name="place_of_death", lookup_expr='icontains')

    gender = filters.CharFilter(field_name="gender", lookup_expr='icontains')

    min_birth_year = filters.NumberFilter(field_name="birth_year", lookup_expr='gte')

    max_birth_year = filters.NumberFilter(field_name="birth_year", lookup_expr='lte')

    min_death_year = filters.NumberFilter(field_name="death_year", lookup_expr='gte')
 
    max_death_year = filters.NumberFilter(field_name="death_year", lookup_expr='lte')

    alive = filters.BooleanFilter(field_name="death_year", lookup_expr='isnull')

    class Meta:
        model = Artist
        fields = ['name', 'birthplace', 'min_birth_year', 'max_death_year', 'deathplace', 'gender',
                  'min_death_year', 'max_death_year', 'alive']

class ArtworkFilter(filters.FilterSet):
    title = filters.CharFilter(field_name="search_title", lookup_expr='icontains')
    medium = filters.CharFilter(field_name="medium",
                                lookup_expr='icontains')

    class Meta:
        model = Artwork
        fields = ['title', 'medium']
