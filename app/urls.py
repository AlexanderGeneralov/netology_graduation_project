from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import ImageViewSet, PublicationViewSet, CommentViewSet, LikeViewSet, pub_list_view

router = SimpleRouter()
router.register('img', ImageViewSet)
router.register('pub', PublicationViewSet)
router.register('com', CommentViewSet)
router.register('like', LikeViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path("pubs/", pub_list_view, name="pub_list_view"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
