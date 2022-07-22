from django.urls import path, include
from rest_framework import routers

from users.views import UserViewSet

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls))
]