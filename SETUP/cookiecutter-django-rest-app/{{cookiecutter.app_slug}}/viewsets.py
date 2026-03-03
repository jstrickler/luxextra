from rest_framework import viewsets

from {{cookiecutter.app_slug}}.models import * # change to only needed models
from {{cookiecutter.app_slug}}.api.serializers import *  # change to only needed serializers
from {{cookiecutter.app_slug}}.api.filters import # (optional)  change to only needed serializers

# Create your viewsets here.
#
# examples:
#
#  class MyFirstModelViewSet(viewsets.ModelViewSet):
#      queryset = MyFirstModel.objects.all()
#      serializer_class = MyFirstModelSerializer
#      filter_backends = [DjangoFilterBackend]
#      filterset_class = MyFirstModelFilter
#
#
#  class MySecondModelViewSet(viewsets.ModelViewSet):
#      queryset = MySecondModel.objects.all()
#      serializer_class = MySecondModelSerializer
#      filter_backends = [DjangoFilterBackend]
#      filterset_class = MySecondModelFilter

