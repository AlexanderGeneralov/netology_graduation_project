from rest_framework.permissions import BasePermission, SAFE_METHODS

from .models import Publication


class IsCreatorOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        #if request.method == 'GET':
        #    return True

        if obj.pub_author == request.user:
            return True

        return False


class ImagePermission(BasePermission):

    edit_methods = ['PUT', 'PATCH']

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):

        if request.user.is_superuser:
            return True

        if request.method in SAFE_METHODS:
            return True

        if request.user.id == Publication.objects.get(id=obj.image_to_pub_id).pub_author_id:
            return True

        if request.user.is_staff and request.method not in self.edit_methods:
            return True

        return False


class ImageAuthorPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.id == Publication.objects.get(id=obj.image_to_pub_id).pub_author_id:
            return True
        return False
