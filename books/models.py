from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ngettext_lazy as _
from django.utils import timezone
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=50, )  # verbose_name=_('name'))

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100, )  # verbose_name=_('name')
    description = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatar/', blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, )  # verbose_name=_('user'))
    genre = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE, )  # verbose_name=_('genre'))
    title = models.CharField(max_length=100, )  # verbose_name=_('title'))
    author = models.ForeignKey(Author, related_name='author', on_delete=models.CASCADE, )  # verbose_name=_('author'))
    description = RichTextField()  # verbose_name=_('description'))
    price = models.DecimalField(max_digits=6, decimal_places=3, )  # verbose_name=_('price'))
    cover = models.ImageField(upload_to='cover/', )  # verbose_name=_('cover'))
    favorite = models.ManyToManyField(get_user_model(), related_name='favorite', blank=True)
    release_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE,related_name='comments')
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
