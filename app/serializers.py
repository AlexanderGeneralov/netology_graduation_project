from rest_framework import serializers
from .models import Publication, Comment, Image, Coordinate


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['com_text', 'com_like', 'com_date', 'com_author']


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ['id', 'pub_text', 'pub_author', 'pub_date']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['comment'] = CommentSerializer(instance.comment_author.all(), many=True).data
        representation['image'] = ImageSerializer(instance.images.all(), many=True).data
        return representation
