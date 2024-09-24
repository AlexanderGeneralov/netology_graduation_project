from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views
from .views import ImageViewSet, PublicationViewSet, CommentViewSet


router = SimpleRouter()
router.register('img', ImageViewSet)
router.register('pub', PublicationViewSet)
router.register('com', CommentViewSet)

urlpatterns = [
    path('api/upload_image/', views.upload_image_view, name='upload_image'),
    path('api/', include(router.urls))
]
