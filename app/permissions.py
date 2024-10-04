from rest_framework.permissions import BasePermission, SAFE_METHODS


EDIT_METHODS = ['PUT', 'PATCH']


class PublicationPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user.id == obj.pub_author.id:
            return True
        if request.user.is_staff and request.method not in EDIT_METHODS:
            return True


class ImagePermission(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user.id == obj.image_to_pub.pub_author.id:
            return True
        if request.user.is_staff and request.method not in EDIT_METHODS:
            return True


class CoordinatePermission(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user.id == obj.coor_to_pub.pub_author.id:
            return True
        if request.user.is_staff and request.method not in EDIT_METHODS:
            return True
        return False


class CommentPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user.id == obj.com_author.id:
            return True
        if request.user.is_staff and request.method not in EDIT_METHODS:
            return True
