from django.urls import path, include
from rest_framework import routers

from books.views import BookViewSet
from users.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'api/books', BookViewSet)
router.register(r'api/users', UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]