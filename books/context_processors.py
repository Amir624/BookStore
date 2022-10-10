from .models import Author, Category, Book


def author_list(request):
    return {
        'authors': Author.objects.all(),
        'category': Category.objects.all(),



            }
