from django.urls import include
from django.urls import re_path, path
from django.conf import settings

urlpatterns = [
    re_path(r'^', include('zelthy.apps.appauth.urls')),
    re_path(r'api/auth/', include('knox.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
    re_path(r'^((?:[\w\-:.,]+/)*)$', include('zelthy.apps.dynamic_models.urls')),
        
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
