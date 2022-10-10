from django.urls import path
from .views import AuthorList,detail_author, ticket

urlpatterns = [
    path('author/', AuthorList.as_view(), name='author'),
    path('<int:pk>/detail/author/',detail_author, name='detail_author'),
    path('contact/', ticket, name='contact_us'),
]