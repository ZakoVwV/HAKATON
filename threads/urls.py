# forum/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ThreadViewSet

router = DefaultRouter()
router.register(r'threads', ThreadViewSet)  # Это указывает на обработку всех типов запросов

urlpatterns = [
    path('', include(router.urls)),
]