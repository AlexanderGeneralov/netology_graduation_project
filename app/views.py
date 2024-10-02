from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Image, Publication, Comment, Coordinate
from .permissions import IsCreatorOrReadOnly
from .serializers import ImageSerializer, PublicationSerializer, CommentSerializer, \
    CoordinateSerializer


@api_view(['POST'])
def upload_image_view(request):
    if request.method == 'POST':
        data = request.data
        serializer = ImageSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            return Response(data=data)
        return Response(serializer.errors, status=404)


class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return []
        if self.action in ["create"]:
            return [IsAuthenticated()]
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsCreatorOrReadOnly()]
        return []


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CoordinateViewSet(viewsets.ModelViewSet):
    queryset = Coordinate.objects.all()
    serializer_class = CoordinateSerializer
