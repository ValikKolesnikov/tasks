from django.urls import path, re_path
from . import views

urlpatterns = [
    path('users/', views.UserPost.as_view(), name='user_post'),
    path('users/<int:id>/', views.UserDetail.as_view(), name='user_detail'),
    path('users/current/', views.CurrentUserDetail.as_view(), name='current_user'),
    path('users/<int:id>/reset-password/', views.PasswordReset.as_view(), name='reset-password'),
    path('tokens/obtain/', views.ObtainToken.as_view(), name='obtain_token'),
    path('tokens/verify/', views.VerifyToken.as_view(), name='verify_token'),

]
