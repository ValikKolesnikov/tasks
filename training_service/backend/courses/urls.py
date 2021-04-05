from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'courses', views.CourseViewSet, basename='courses')
router.register(r'courses', views.CourseViewSet, basename='courses')

urlpatterns = [
]

urlpatterns += router.urls
