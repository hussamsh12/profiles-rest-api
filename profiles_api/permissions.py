from rest_framework import permissions



class UpdateOwnProfile(permissions.BasePermission):
    """Allow Users to edit their own profile"""

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.id == obj.id


class UpdateOwnStatus(permissions.BasePermission):
    """Permission Class for profile feed item"""

    def has_object_permission(self, request, view, obj):
        """Check if the user is trying to update their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True
        print("In has_object_permission")
        print(request.user.id)
        print(obj.user_profile.id)
        return request.user.id == obj.user_profile.id