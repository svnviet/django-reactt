from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required
from rest_framework import routers
from .views import FilmApiView

router = routers.DefaultRouter()
router.register(r'blogs', FilmApiView, 'blogs')
api_path = router.urls
urlpatterns = [
    path("", include(api_path)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
