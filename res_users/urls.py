from rest_framework import routers
from .views import UserViewSet, RegisterViewSet, UserProfileViewSet
from django.urls import path, include
from .models import UserProfile

router = routers.DefaultRouter()
router.register("users", UserViewSet)
router.register("profile", UserProfileViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterViewSet.as_view()),
]
