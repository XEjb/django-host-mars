from django.conf.urls.static import static
from yuki import settings
from django.contrib import admin
from django.urls import path, include
from yukiko.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('yukiko.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound