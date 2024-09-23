from django.contrib import admin

from .models import Publication, Comment, Image, Coordinate


admin.site.register(Publication)
admin.site.register(Comment)
admin.site.register(Image)
admin.site.register(Coordinate)
