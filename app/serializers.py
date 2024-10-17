from rest_framework import serializers
from .models import Publication, Comment, Image, Like

from geopy.geocoders import Nominatim


class ImageSerializer(serializers.ModelSerializer):
    """
    Class to describe image serializer.
    """
    class Meta:
        model = Image
        fields = ['id', 'image', 'image_to_pub']


class CommentSerializer(serializers.ModelSerializer):
    """
    Class to describe comment serializer.
    """
    class Meta:
        model = Comment
        fields = ['com_text', 'com_like', 'com_date', 'com_author', 'com_to_pub']
        read_only_fields = ['com_author']

    def create(self, validated_data):
        """
        Method to implicitly add user to serialized data.
        :param validated_data: data from http request
        :return: method of parent class
        """
        validated_data['com_author'] = self.context['request'].user
        return super().create(validated_data)


class PublicationSerializer(serializers.ModelSerializer):
    """
    Class to describe publication serializer.
    """
    comment = CommentSerializer(source='comments', many=True, read_only=True)  # adding extra field
    image = ImageSerializer(source='images', many=True, read_only=True)  # adding extra field
    likes_count = serializers.SerializerMethodField()  # adding extra field

    class Meta:
        model = Publication
        fields = ['id', 'pub_text', 'pub_author', 'pub_date', 'coor_text', 'coor_adress', 'coor_coordinates', 'comment', 'image', 'likes_count']
        read_only_fields = ['pub_author', 'coor_adress', 'coor_coordinates']

    def get_likes_count(self, obj):
        """
        Method to calculate number of likes to publication
        :param obj: publication model instance
        :return: object (likes_count) to be serialized as extra field to publication
        """
        return obj.likes.filter(like_bool=True).count()

    def create(self, validated_data):
        """
        Method to implicitly add geodata and user to serialized data.
        :param validated_data: data from http request
        :return: method of parent class
        """
        coor_text = validated_data['coor_text']
        geolocator = Nominatim(user_agent='epictalk')
        location = geolocator.geocode(coor_text)
        coor_adress = location.address
        coor_coordinates = f'{location.latitude}, {location.longitude}'
        validated_data['coor_adress'] = coor_adress
        validated_data['coor_coordinates'] = coor_coordinates
        validated_data['pub_author'] = self.context['request'].user
        return super().create(validated_data)


class LikeSerializer(serializers.ModelSerializer):
    """
    Class to describe like serializer.
    """
    class Meta:
        model = Like
        fields = ['id', 'like_bool', 'like_to_pub', 'like_author']
        read_only_fields = ['like_author']

    def create(self, validated_data):
        """
        Method to implicitly add user to serializer.
        :param validated_data: data from http request
        :return: method of parent class
        """
        author = self.context['request'].user
        like_to_pub = validated_data['like_to_pub']

        # check if author already put 'like' to publication
        # if author did, exception will be raised
        if Like.objects.filter(like_author=author, like_to_pub=like_to_pub).exists():
            raise serializers.ValidationError('do not fool with likes)')

        validated_data['like_author'] = self.context['request'].user
        return super().create(validated_data)
