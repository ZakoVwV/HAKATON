from  django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import CategoryViewset

router = DefaultRouter()
router.register('', CategoryViewset)

urlpatterns = [
    path('', include(router.urls)),
]