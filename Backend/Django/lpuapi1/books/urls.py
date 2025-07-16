from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, CarViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'cars', CarViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
