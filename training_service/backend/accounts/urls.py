from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'users/$', views.UserList.as_view(), name='user_list'),
    path('users/<int:id>', views.UserDetail.as_view(), name='user_detail'),
    path('groups/', views.GroupList.as_view(), name='group_list'),
    path('users/current', views.CurrentUserDetail.as_view(), name='current_user'),
    path('users/<int:id>/reset-password', views.PasswordReset.as_view(), name='reset-password'),
    re_path(r'users/count/$', views.UserCount.as_view(), name='user_count'),
    re_path(r'users/count/registered/$', views.UserRegisteredCount.as_view(), name='user_registered'),
    path('users/groups', views.UserGroups.as_view(), name='users_groups'),
    path('groups/user-count', views.GroupUsersCount.as_view(), name='groups_user_count'),
    path('tokens/obtain', views.ObtainToken.as_view(), name='obtain_token'),
    path('tokens/verify', views.VerifyToken.as_view(), name='verify_token'),

]
