from rest_framework import permissions


class CurrentUserOrAdminUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user

    def has_object_permission(self, request, view, obj):
        user = request.user
        return user == obj or user.is_staff
