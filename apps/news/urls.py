from django.urls import path

from apps.news.views import upvote_news, unvote_news, CommentsViewSet, NewsView
from rest_framework import routers
from django.urls import include

router = routers.SimpleRouter()
router.register('comments', CommentsViewSet, 'comments')
router.register('news', NewsView, 'news')


urlpatterns = [
    path('upvote/<int:pk>/', upvote_news, name='upvote_news'),
    path('unvote/<int:pk>/', unvote_news, name='unvote_news'),
    path('', include(router.urls)),
]
