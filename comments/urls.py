from rest_framework.routers import DefaultRouter

from .views import CommentViewSet

from django.urls import path, include

router = DefaultRouter()
router.register('', CommentViewSet)

urlpatterns = [
    path('', include(router.urls))
]