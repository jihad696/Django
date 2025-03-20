from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import track_update, TrackViewSet

router = DefaultRouter()
router.register(r'tracks', TrackViewSet)

urlpatterns = [
    path('tracks/<int:pk>/', track_update, name='api-track-update'),
    path('', include(router.urls)),
]