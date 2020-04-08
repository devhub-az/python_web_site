from rest_framework.permissions import BasePermission,SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self,request,view,obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user