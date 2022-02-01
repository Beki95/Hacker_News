from django.db import models


# Create your models here.
class CreatedateModel(models.Model):
    creation_date = models.DateTimeField(
        'created date', auto_now_add=True
    )

    class Meta:
        abstract = True


class News(CreatedateModel):
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
        db_table = 'news'
    title = models.CharField('title', max_length=255, null=False, blank=False)
    link = models.URLField('link', max_length=500, null=False, blank=False)
    author = models.CharField(max_length=50)
    qs_vote = models.IntegerField(blank=True, default=0)


class Comment(CreatedateModel):
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        db_table = 'comment'

    news = models.ForeignKey(News, on_delete=models.CASCADE, blank=False,
                             verbose_name='news', related_name='news_comment')
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, blank=False,
                               verbose_name='author', related_name='author_comment')
    description = models.TextField()
