from django.db import models


class Post(models.Model):
    author = models.CharField(max_length=150, blank=True)
    header = models.CharField(max_length=60)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=150, blank=True)
    content = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.headline

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
