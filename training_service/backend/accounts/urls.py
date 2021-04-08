from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='users')
router.register(r'participations', views.ParticipationViewSet, basename='users_participation')
router.register(r'groups', views.GroupViewSet, basename='groups')

urlpatterns = [
    path('tokens/obtain/', views.ObtainTokenView.as_view(), name='token_obtain'),
    path('tokens/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
    path('tokens/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh')
]

urlpatterns += router.urls
