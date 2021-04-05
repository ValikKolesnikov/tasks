from rest_framework import permissions


class CurrentUserOrAdminUser(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == 'teacher_create' or view.action == 'student_create':
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        user = request.user
        return user == obj or user.is_staff
