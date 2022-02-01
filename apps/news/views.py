from rest_framework import status

# Create your views here.
from rest_framework import mixins
from apps.news.mixins import UpvoteUnvoteMixins
from apps.news.models import News, Comment
from apps.news.serializers import NewsSerializer, CommentsSerializer, RetrieveNewsSerializer
from django.db.models import Count, F
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


class NewsView(

    viewsets.ReadOnlyModelViewSet
):

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return RetrieveNewsSerializer
        return NewsSerializer

    queryset = News.objects.prefetch_related('news_comment').annotate(
        comments_count=Count('news_comment')).order_by('-qs_vote')


class UpvoteNews(UpvoteUnvoteMixins):

    def update(self, request, *args, **kwargs):
        data = super()._pre_update(request, **kwargs)
        if data.get('error', False):
            return Response(status.HTTP_404_NOT_FOUND)
        if data.get('bool'):
            return Response(status.HTTP_400_BAD_REQUEST)
        # increase rating
        instance, up_submissions = data.get('instance'), data.get('up_submissions')
        instance.update(qs_vote=F('qs_vote') + 1)
        up_submissions.add(instance.first())
        return Response(status=status.HTTP_200_OK)


upvote_news = UpvoteNews.as_view()


class UnvoteNews(UpvoteUnvoteMixins):

    def update(self, request, *args, **kwargs):
        data = super()._pre_update(request, **kwargs)
        if data.get('error', False):
            return Response(status.HTTP_404_NOT_FOUND)
        if not data.get('bool'):
            return Response(status.HTTP_400_BAD_REQUEST)
        # remove rating
        instance, up_submissions = data.get('instance'), data.get('up_submissions')
        instance.update(qs_vote=F('qs_vote') - 1)
        up_submissions.remove(instance.first())
        return Response(status=status.HTTP_200_OK)


unvote_news = UnvoteNews.as_view()


class CommentsViewSet(
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = CommentsSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Comment.objects.filter()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={"author": request.user})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = get_object_or_404(Comment, pk=kwargs.get('pk'))
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(True)
        return Response(serializer.data, status=status.HTTP_200_OK)
