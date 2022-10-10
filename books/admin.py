from django.contrib import admin
from .models import Author,Category, Book,Comment
from jalali_date.admin import ModelAdminJalaliMixin,StackedInlineJalaliMixin


admin.site.register(Author)

admin.site.register(Category)
admin.site.register(Comment)


class CommentInline(admin.StackedInline):
    model = Comment
    fields = ('user', 'book', 'text', )
    extra = 0


@admin.register(Book)
class BookAdmin(ModelAdminJalaliMixin,StackedInlineJalaliMixin,admin.ModelAdmin):
    list_display = ['title', 'author', ]

    inlines = [
        CommentInline,
    ]
