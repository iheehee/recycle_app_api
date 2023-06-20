from rest_framework import permissions

class IsSelf(permissions.BasePermission):
    
    def has_object_permission(self, request, view, user):
    
        return user == request.user