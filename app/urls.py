from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views
from .views import ImageViewSet, PublicationViewSet, CommentViewSet, CoordinateViewSet

router = SimpleRouter()
router.register('img', ImageViewSet)
router.register('pub', PublicationViewSet)
router.register('com', CommentViewSet)
router.register('coor', CoordinateViewSet)

urlpatterns = [
    path('api/upload_image/', views.upload_image_view, name='upload_image'),
    path('api/', include(router.urls))
]
