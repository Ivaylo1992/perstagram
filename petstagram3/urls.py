from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from petstagram3 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("petstagram3.common.urls")),
    path("accounts/", include("petstagram3.accounts.urls")),
    path("pets/", include("petstagram3.pets.urls")),
    path("photos/", include("petstagram3.photos.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)