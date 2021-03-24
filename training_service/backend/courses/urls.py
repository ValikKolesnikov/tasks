from django.urls import path, re_path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register(r'users', views.UserViewSet, basename='users')
# router.register(r'groups', views.GroupViewSet, basename='groups')
# router.register(r'tokens', views.TokenViewSet, basename='tokens')

urlpatterns = [
]

urlpatterns += router.urls
