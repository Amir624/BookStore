from django.shortcuts import render, get_object_or_404
from django.views import generic
from books.models import Author, Book
from .forms import ContactForm
from django.contrib import messages
import ghasedakpack


class AuthorList(generic.ListView):
    model = Author
    template_name = 'pages/author_list.html'
    context_object_name = 'authors'


def detail_author(request, pk):
    authors = get_object_or_404(Author, pk=pk)
    book_author = Book.objects.filter(author=pk)
    return render(request, 'pages/detail_author.html', {'authors': authors, 'book_author': book_author})


def ticket(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user_messages =  f"یک پیام در سایت ثبت شد نام کاربر:- {data['first_name']} -متن پیام: {data['text']}  "
            form.save()
            sms = ghasedakpack.Ghasedak("96717c350e773ed6410cfe43799eb5951d1b0cfb6fc750d5b2fdff5d73d03081")
            sms.send({'message': user_messages, 'receptor': "09227226142", 'linenumber': "10008566"})
            messages.success(request, 'پیام شما با موفقیت ارسال شد')
    else:
        form = ContactForm()

    return render(request, 'pages/contact_us.html', {'form': form})
