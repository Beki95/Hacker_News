from rest_framework import serializers as s

from apps.news.models import News, Comment


class CommentsSerializer(s.ModelSerializer):
    author = s.CharField(read_only=True)

    class Meta:
        model = Comment
        fields = 'id', 'news', 'author', 'description', 'creation_date'

    def create(self, validated_data):
        validated_data['author'] = self.context.get("author")
        super(CommentsSerializer, self).create(validated_data)
        return validated_data


class NewsSerializer(s.ModelSerializer):
    comments_count = s.IntegerField()

    class Meta:
        model = News
        fields = 'id', 'title', 'link', 'author', 'qs_vote', \
                 'comments_count', 'creation_date'


class RetrieveNewsSerializer(NewsSerializer):

    def to_representation(self, instance):
        data = super(RetrieveNewsSerializer, self).to_representation(instance)
        data['comments'] = CommentsSerializer(instance.news_comment, many=True).data
        return data
