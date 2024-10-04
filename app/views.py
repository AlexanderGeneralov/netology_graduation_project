from rest_framework import viewsets

from .models import Image, Publication, Comment, Coordinate
from .permissions import PublicationPermission, ImagePermission, CommentPermission, CoordinatePermission
from .serializers import ImageSerializer, PublicationSerializer, CommentSerializer, \
    CoordinateSerializer


class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    permission_classes = [PublicationPermission]


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [ImagePermission]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [CommentPermission]


class CoordinateViewSet(viewsets.ModelViewSet):
    queryset = Coordinate.objects.all()
    serializer_class = CoordinateSerializer
    permission_classes = [CoordinatePermission]
