from rest_framework.permissions import BasePermission, SAFE_METHODS


EDIT_METHODS = ['PUT', 'PATCH']  # methods for editing


class PublicationPermission(BasePermission):
    """
    Class describes authentication and permission rules.
    """
    def has_permission(self, request, view):
        """
        Methods to check user authentication
        :param request: request object from http request
        :param view: view object of PublicationViewSet
        :return: True
        """
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        """
        Method to check if user has permission for object
        :param request: request object from http request
        :param view: view object of PublicationViewSet
        :param obj: instance of a model
        :return: True
        """
        if request.method in SAFE_METHODS:
            return True
        if request.user.id == obj.pub_author.id:
            return True
        if request.user.is_staff and request.method not in EDIT_METHODS:
            return True


class ImagePermission(BasePermission):
    """
    Class describes authentication and permission rules.
    """
    def has_permission(self, request, view):
        """
        Methods to check user authentication
        :param request: request object from http request
        :param view: view object of ImageViewSet
        :return: True
        """
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        """
        Method to check if user has permission for object
        :param request: request object from http request
        :param view: view object of ImageViewSet
        :param obj: instance of a model
        :return: True
        """
        if request.method in SAFE_METHODS:
            return True
        if request.user.id == obj.image_to_pub.pub_author.id:
            return True
        if request.user.is_staff and request.method not in EDIT_METHODS:
            return True


class CoordinatePermission(BasePermission):
    """
    Class describes authentication and permission rules.
    """
    def has_permission(self, request, view):
        """
        Methods to check user authentication
        :param request: request object from http request
        :param view: view object of CoordinateViewSet
        :return: True
        """
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        """
        Method to check if user has permission for object
        :param request: request object from http request
        :param view: view object of CoordinateViewSet
        :param obj: instance of a model
        :return: True
        """
        if request.method in SAFE_METHODS:
            return True
        if request.user.id == obj.coor_to_pub.pub_author.id:
            return True
        if request.user.is_staff and request.method not in EDIT_METHODS:
            return True
        return False


class CommentPermission(BasePermission):
    """
    Class describes authentication and permission rules.
    """
    def has_permission(self, request, view):
        """
        Methods to check user authentication
        :param request: request object from http request
        :param view: view object of CommentViewSet
        :return: True
        """
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        """
        Method to check if user has permission for object
        :param request: request object from http request
        :param view: view object of CommentViewSet
        :param obj: instance of a model
        :return: True
        """
        if request.method in SAFE_METHODS:
            return True
        if request.user.id == obj.com_author.id:
            return True
        if request.user.is_staff and request.method not in EDIT_METHODS:
            return True


class LikePermission(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True
        if request.user.id == obj.like_to_pub.id:
            return True
        if request.user.is_staff and request.method not in EDIT_METHODS:
            return True
