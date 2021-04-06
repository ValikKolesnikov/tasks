from rest_framework import permissions


class IsOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == 'create':
            return True
        return request.user

    def has_object_permission(self, request, view, obj):
        return request.user == obj
