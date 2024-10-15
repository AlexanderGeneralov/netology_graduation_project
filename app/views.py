from rest_framework import viewsets

from .models import Image, Publication, Comment, Coordinate, Like
from .permissions import PublicationPermission, ImagePermission, CommentPermission, CoordinatePermission, LikePermission
from .serializers import ImageSerializer, PublicationSerializer, CommentSerializer, \
    CoordinateSerializer, LikeSerializer


class PublicationViewSet(viewsets.ModelViewSet):
    """
    Class to described publication view set.
    """
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    permission_classes = [PublicationPermission]


class ImageViewSet(viewsets.ModelViewSet):
    """
    Class to described image view set.
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [ImagePermission]


class CommentViewSet(viewsets.ModelViewSet):
    """
    Class to described comment view set.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [CommentPermission]


class CoordinateViewSet(viewsets.ModelViewSet):
    """
    Class to described coordinate view set.
    """
    queryset = Coordinate.objects.all()
    serializer_class = CoordinateSerializer
    permission_classes = [CoordinatePermission]


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [LikePermission]
