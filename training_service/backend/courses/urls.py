from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'courses', views.CourseViewSet, basename='courses')
router.register(r'tests', views.TestViewSet, basename='tests')
router.register(r'reading_materials', views.ReadingMaterialViewSet, basename='reading_materials')

urlpatterns = [
]

urlpatterns += router.urls
