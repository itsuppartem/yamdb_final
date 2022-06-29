from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet, CommentViewSet, ConfirmationCodeApiView,
                    GenreViewSet, ReviewViewSet, TitleViewSet, TokenApiView,
                    UserViewSet)

router = DefaultRouter()

router.register('users', UserViewSet)
# router.register('users/<str:username>', UsernameViewSet)

router.register(
    r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet, basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments'
)

router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'genres', GenreViewSet, basename='genres')
router.register(r'titles', TitleViewSet, basename='titles')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', ConfirmationCodeApiView.as_view(), name='signup'),
    path('v1/auth/token/', TokenApiView.as_view(), name='token'),
]
