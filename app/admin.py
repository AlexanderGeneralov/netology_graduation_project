from django.contrib import admin

from .models import Publication, Comment, Image, Coordinate, Like

admin.site.register(Publication)
admin.site.register(Comment)
admin.site.register(Image)
admin.site.register(Coordinate)
admin.site.register(Like)
