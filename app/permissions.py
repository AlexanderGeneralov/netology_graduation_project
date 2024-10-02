from rest_framework.permissions import BasePermission


class IsCreatorOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        #if request.method == 'GET':
        #    return True

        if obj.pub_author == request.user:
            return True

        return False