from django.urls import path
from .views import HomePage, detail_page, favorite_book, favorite_list,search_bar,category, filter_books, sort_book
urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('<int:pk>/detail/', detail_page, name='detail_page'),
    path('<int:pk>/favorite/', favorite_book, name='favorite'),
    path('favorite/list', favorite_list, name='favorite_list'),
    path('search', search_bar, name='search'),
    path('<int:pk>/category/', category, name='category'),
    path('filter/', filter_books, name='filter'),
    path('sort/', sort_book, name='sort_book'),

]
