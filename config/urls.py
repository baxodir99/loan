from django.contrib import admin
from django.urls import path, include
from .schema import swagger_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.structure.urls')),
    path('api/', include('apps.user.urls')),
]


urlpatterns += swagger_urlpatterns