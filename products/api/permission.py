from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        #print('list or create ...........', request, view)
        if request.user.is_authenticated:
            return True
        return False
    

    def has_object_permission(self, request, view, obj):
        #print('detail.....[',view)
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user == request.user 