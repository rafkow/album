from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('photos', views.get_photos),
    path('photo/add', views.post_photo),
    path('photos/add', views.post_photos),
    path('photo/update', views.put_photo),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

