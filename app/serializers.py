from rest_framework import serializers
from .models import Publication, Comment, Image, Coordinate

from geopy.geocoders import Nominatim


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ['id', 'image', 'image_to_pub']


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['com_text', 'com_like', 'com_date', 'com_author', 'com_to_pub']


class CoordinateSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        coor_text = validated_data['coor_text']
        geolocator = Nominatim(user_agent='epictalk')
        location = geolocator.geocode(coor_text)
        coor_adress = location.address
        coor_coordinates = f'{location.latitude}, {location.longitude}'
        validated_data['coor_adress'] = coor_adress
        validated_data['coor_coordinates'] = coor_coordinates
        return super().create(validated_data)

    class Meta:
        model = Coordinate
        fields = ['id', 'coor_text', 'coor_adress', 'coor_to_pub']


class PublicationSerializer(serializers.ModelSerializer):

    comment = CommentSerializer(source='comments', many=True, read_only=True)
    image = ImageSerializer(source='images', many=True, read_only=True)
    coordinate = CoordinateSerializer(source='coordinates', many=True, read_only=True)

    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Publication
        fields = ['id', 'pub_text', 'pub_author', 'pub_date', 'comment', 'image', 'likes_count', 'coordinate']

    def get_likes_count(self, obj):
        return obj.comments.filter(com_like=True).count()
