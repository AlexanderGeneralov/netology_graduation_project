from django.contrib.auth.models import User
from django.db import models


class Publication(models.Model):
    """
    Class to describe publication model.
    """
    pub_text = models.TextField(null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    pub_author = models.ForeignKey(User, on_delete=models.CASCADE)
    coor_text = models.CharField(null=True, blank=True)
    coor_adress = models.CharField(null=True, blank=True)
    coor_coordinates = models.CharField(null=True, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"
        ordering = ["-pub_date"]


class Comment(models.Model):
    """
    Class to describe comment model.
    """
    com_text = models.TextField(null=True, blank=True)
    com_like = models.BooleanField(default=False)
    com_author = models.ForeignKey(User, on_delete=models.CASCADE)
    com_to_pub = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name='comments')
    com_date = models.DateTimeField(auto_now_add=True, null=True)


class Image(models.Model):
    """
    Class to describe image model.
    """
    image = models.ImageField(upload_to='images', null=True)
    image_to_pub = models.ForeignKey(Publication, on_delete=models.CASCADE, null=True, related_name='images')


class Like(models.Model):
    """
    Class to describe like model
    """
    like_bool = models.BooleanField(default=False)
    like_to_pub = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name='likes')
    like_author = models.ForeignKey(User, on_delete=models.CASCADE)
