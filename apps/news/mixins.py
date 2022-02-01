from rest_framework import generics, status

# Create your views here.
from apps.news.models import News
from rest_framework.permissions import IsAuthenticated


class UpvoteUnvoteMixins(generics.UpdateAPIView):
    serializer_class = None
    permission_classes = (IsAuthenticated,)

    def _pre_update(self, request, **kwargs) -> dict:
        instance = News.objects.filter(id=kwargs.get('pk'))
        if not instance:
            return {'error': status.HTTP_400_BAD_REQUEST}
        up_submissions = request.user.upvoted_submissions
        data = {
            'bool': bool(up_submissions.filter(id=instance.first().id)),
            'instance': instance,
            'up_submissions': up_submissions
        }
        return data
