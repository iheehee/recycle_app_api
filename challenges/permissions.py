from rest_framework import permissions
from core.authentication import JWTAuthentication


class IsAuth(permissions.BasePermission):
    def has_object_permission(self, request, view, profile):
        decoded = JWTAuthentication.authenticate(self, request)
        return profile.nickname == decoded.id
