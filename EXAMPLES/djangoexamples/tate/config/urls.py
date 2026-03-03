"""tate URL Mapping

The `urlpatterns` list maps URLs to views. More information:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

Function views:
    1. Add an import:  from my_app import views
    2. Add entry to urlpatterns:  path('view_name', views.view_name, name='view_name')

Class-based views:
    1. Add an import:  from my_app.views import Home
    2. Add entry to urlpatterns:  path('view_name', ViewName.as_view(), name='view_name')

Including another (usually an app's) URLconf:
    1. Import the include() function: from django.urls import url, include
    2. Add a URL to urlpatterns:  path('appname', include('app.urls', ))
    Path may be blank; in that case only the app URL is used
"""
from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from views import HomeView

# site-wide route mapping
urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # docs
    # path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # local
    path('', HomeView.as_view(), name="home"),

    path('classviews/', include('classviews.urls')),
    path('api/', include('api.urls')),
    path('fbv/', include('functionviews.urls')),
    path('formsdemo/', include('formsdemo.urls')),
    path('messagesdemo/', include('messagesdemo.urls')),
]

# include Django Debug toolbar if DEBUG is set
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__', include(debug_toolbar.urls)),
    ] + urlpatterns

