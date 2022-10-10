from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views import generic
from .models import Book, Comment, Author
from .forms import CommentForm
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.views import login_required
from .filters import BookFilter
from posts.models import Post

class HomePage(generic.ListView):
    model = Book
    template_name = 'books/home.html'
    context_object_name = 'books'


def detail_page(request, pk):
    book = get_object_or_404(Book, pk=pk)
    comment = book.comments.all()
    book_author = Book.objects.filter(author=pk)
    is_favorite = False
    if book.favorite.filter(id=request.user.id).exists():
        is_favorite = True

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.book = book
            new_form.user = request.user
            new_form.save()
            form = CommentForm
    else:
        form = CommentForm()

    return render(request, 'books/detail_page.html',
                  {'book': book, 'comments': comment, 'form': form, 'favorite': is_favorite,
                   'book_author': book_author})


@login_required()
def favorite_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if not book.favorite.filter(id=request.user.id).exists():
        book.favorite.add(request.user)
        messages.success(request, 'به لیست علاقه مندی اضافه شد')
    else:
        book.favorite.remove(request.user)
        messages.success(request, 'از لیست علاقه مندی حذف شد')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required()
def favorite_list(request):
    user = request.user
    favorite_books = user.favorite.all()
    return render(request, 'books/favorite_list.html', {'favorite_books': favorite_books})


def search_bar(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        book = Book.objects.filter(
            Q(title__contains=searched) | Q(author__name__contains=searched) | Q(genre__name__contains=searched))
        post = Post.objects.filter(title__contains=searched)
        return render(request, 'books/search_result.html', {'searched': searched, 'books': book, "post": post})
    else:
        return render(request, 'books/search_result.html')


def category(request, pk):
    cat = Book.objects.filter(genre=pk)
    return render(request, 'books/category.html', {'category': cat})


def filter_books(request):
    book_list = Book.objects.all()
    book_filter = BookFilter(request.POST, queryset=book_list)
    return render(request, 'books/filter_result.html', {'filter': book_filter, })


def sort_book(request):
    sort_by = request.GET.get('sort', 'low')
    if sort_by == 'low':
        product = Book.objects.filter().order_by('price')

    elif sort_by == 'new':
        product = Book.objects.filter().order_by('-release_date')
    # elif sort_by == 'old':
    #     product = Book.objects.filter().order_by('create_datetime')
    return render(request, 'books/sort_list.html', {'sort': sort_by, 'product': product})