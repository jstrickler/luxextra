from django.urls import include, path
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from . import views, viewsets

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'artists', viewsets.ArtistViewSet, basename='artist')
router.register(r'artworks', viewsets.ArtworkViewSet, basename='artwork')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # drf-spectacular schemas


    # routes from querysets
    path('vs/', include(router.urls)),

    # route from function-based view
    path('artists-fbv/<str:pk>', views.artist, name='artists-fbv'),

    # routes from class-based views
    path('artists', views.ArtistList.as_view(), name='artists'),
    path('artists/<str:pk>', views.ArtistDetail.as_view(), name='artists-detail'),
    path('artworks', views.ArtworkList.as_view(), name='artworks'),
    path('artworks/<str:pk>', views.ArtworkDetail.as_view(), name='artworks-detail'),

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='api:schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='api:schema'), name='redoc'),
]

