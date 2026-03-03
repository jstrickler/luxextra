from django_filters import rest_framework as filters
from {{cookiecutter.app_slug}}.models import *  # change to only required models

#  class MyFirstModelFilter(filters.FilterSet):
#      name = filters.CharFilter(field_name="name", lookup_expr='icontains')
#      birthplace = filters.CharFilter(field_name="place_of_birth", lookup_expr='icontains')
#
#      """MAX BIRTH YEAR"""
#      min_birth_year = filters.NumberFilter(field_name="birth_year", lookup_expr='gte')
#
#
#      max_birth_year = filters.NumberFilter(field_name="birth_year", lookup_expr='lte')
#
#      min_death_year = filters.NumberFilter(field_name="death_year", lookup_expr='gte')
#      max_death_year = filters.NumberFilter(field_name="death_year", lookup_expr='lte')
#
#      alive = filters.BooleanFilter(field_name="death_year", lookup_expr='isnull')
#
#
#      class Meta:
#          model = MyFirstModel
#          fields = ["field1", "field2,]  # ...
#
#  class MySecondModelFilter(filters.FilterSet):
#      title = filters.CharFilter(field_name="title", lookup_expr='icontains')
#
#      class Meta:
#          model = MySecondModel
#          fields = ["field1", "field2",]  # ...
