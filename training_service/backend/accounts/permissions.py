from rest_framework import permissions


class IsOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == 'create':
            return True
        return request.user

    def has_object_permission(self, request, view, obj):
        return request.user == obj


class CurrentUserIdOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        user_id = request.query_params.get('user_id')
        if user_id:
            return request.user.id == int(user_id) or request.user.is_staff
        return request.user.is_staff
