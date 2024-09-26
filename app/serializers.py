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

    comment = CommentSerializer(source='comments', many=True, read_only=True)
    image = ImageSerializer(source='images', many=True, read_only=True)

    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Publication
        fields = ['id', 'pub_text', 'pub_author', 'pub_date', 'comment', 'image', 'likes_count']

    def get_likes_count(self, obj):
        return obj.comments.filter(com_like=True).count()
