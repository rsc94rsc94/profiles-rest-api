from rest_framework import permissions



class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile."""

    def has_object_permission(self,reqest,view,obj):
        """Check user is trying to edit their own profile."""


        if reqest.method in permissions.SAFE_METHODS:
            return True;
        return obj.id == reqest.user.id
        
