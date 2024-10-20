from rest_framework import viewsets

from .models import Image, Publication, Comment, Like
from .permissions import PublicationPermission, ImagePermission, CommentPermission, LikePermission
from .serializers import ImageSerializer, PublicationSerializer, CommentSerializer, LikeSerializer


class PublicationViewSet(viewsets.ModelViewSet):
    """
    Class to describe publication view set.
    """
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    permission_classes = [PublicationPermission]


class ImageViewSet(viewsets.ModelViewSet):
    """
    Class to describe image view set.
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [ImagePermission]


class CommentViewSet(viewsets.ModelViewSet):
    """
    Class to describe comment view set.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [CommentPermission]


class LikeViewSet(viewsets.ModelViewSet):
    """
    Class to describe lise view set
    """
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [LikePermission]
