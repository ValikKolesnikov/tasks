from django.urls import path, re_path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='users')
router.register(r'groups', views.GroupViewSet, basename='groups')
# router.register(r'tokens', views.TokenViewSet, basename='tokens')

urlpatterns = [
    path('tokens/obtain/', views.ObtainTokenViewSet.as_view(), name='token_obtain'),
    path('tokens/verify/', views.VerifyTokenViewSet.as_view(), name='token_verify'),
    path('tokens/refresh/', jwt_views.TokenRefreshView, name='token_refresh')
]

urlpatterns += router.urls
