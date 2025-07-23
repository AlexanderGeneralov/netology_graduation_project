from django.contrib import admin

from .models import Publication, Comment, Image, Like


class PublicationAdmin(admin.ModelAdmin):
    list_display = ("pub_text", "pub_date", "pub_author")


class ImageAdmin(admin.ModelAdmin):
    list_display = ("image", "image_to_pub")


admin.site.register(Publication, PublicationAdmin)
admin.site.register(Comment)
admin.site.register(Image, ImageAdmin)
admin.site.register(Like)
