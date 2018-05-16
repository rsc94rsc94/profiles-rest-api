from rest_framework import permissions



class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile."""

    def has_object_permission(self,reqest,view,obj):
        """Check user is trying to edit their own profile."""


        if reqest.method in permissions.SAFE_METHODS:
            return True;
        return obj.id == reqest.user.id

class PostOwnStatus(permissions.BasePermission):
    """Allow user to update thier own status."""

    def has_object_permission(self, request, view, obj):
        """Checks is user is trying to update their own status."""

        if request.method in permissions.SAFE_METHODS:
            return True;
        return obj.user_profile.id == request.user.id
