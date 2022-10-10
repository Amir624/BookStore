from django.urls import path
from .views import ListPosts,detail_post

urlpatterns = [
    path('', ListPosts.as_view(), name='news'),
    path('<int:pk>/news/', detail_post, name='detail_post'),

]
