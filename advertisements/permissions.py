from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsAutherOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == permissions.SAFE_METHODS:
            return True
        return obj.creator == request.user
