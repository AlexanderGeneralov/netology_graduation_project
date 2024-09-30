from django.contrib.auth.models import User
from django.db import models


class Publication(models.Model):
    pub_text = models.TextField(null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    pub_author = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    com_text = models.TextField(null=True, blank=True)
    com_like = models.BooleanField(default=False)
    com_author = models.ForeignKey(User, on_delete=models.CASCADE)
    com_to_pub = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name='comments')
    com_date = models.DateTimeField(auto_now_add=True, null=True)


class Image(models.Model):
    image = models.ImageField(upload_to='images', null=True)
    image_to_pub = models.ForeignKey(Publication, on_delete=models.CASCADE, null=True, related_name='images')


class Coordinate(models.Model):
    coor_text = models.CharField(null=True, blank=True)
    coor_adress = models.CharField(null=True, blank=True)
    coor_coordinates = models.CharField(null=True, blank=True)
    coor_to_pub = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name='coordinates')
