from rest_framework import permissions



class UpdateOwnProfile(permissions.BasePermission):
    """Allow Users to edit their own profile"""

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.id == obj.id

