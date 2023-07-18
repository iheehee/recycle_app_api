from rest_framework import permissions
from core.authentication import JWTAuthentication


class IsAuth(permissions.BasePermission):
    def has_permission(self, request, view):
        decoded = JWTAuthentication.authenticate(self, request)
        if decoded:
            return True
        else:
            return False
