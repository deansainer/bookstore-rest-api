from django.urls import path, include
from rest_framework import routers

from books.views import BookViewSet
from users.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]