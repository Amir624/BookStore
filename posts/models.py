from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField


class Post(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = RichTextField()
    cover = models.ImageField(upload_to='post_cover/')
    is_star = models.BooleanField(default=False, blank=True)
    view_count = models.IntegerField(default=0, blank=True)
    datetime_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class CommentPost(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    datetime_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
