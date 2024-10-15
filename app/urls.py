from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import ImageViewSet, PublicationViewSet, CommentViewSet, CoordinateViewSet, LikeViewSet

router = SimpleRouter()
router.register('img', ImageViewSet)
router.register('pub', PublicationViewSet)
router.register('com', CommentViewSet)
router.register('coor', CoordinateViewSet)
router.register('like', LikeViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]
