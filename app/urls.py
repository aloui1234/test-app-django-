from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LabelViewSet, AnnotationViewSet

router = DefaultRouter()
router.register(r'labels', LabelViewSet)
router.register(r'annotations', AnnotationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]