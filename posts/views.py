from django.shortcuts import render, get_object_or_404
from .models import Post, CommentPost
from django.views import generic
from .forms import CommentForm
from django.urls import reverse_lazy


class ListPosts(generic.ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'post'


def detail_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment = post.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.post = post
            new_form.user = request.user
            new_form.save()
            form = CommentForm()
    else:
        form = CommentForm()

    return render(request, 'posts/post_detail.html', {'comments_post': comment, "forms": form, "post":post})














#
# class PostDetailView(generic.DetailView):
#     model = Post
#     template_name = 'posts/post_detail.html'
#     context_object_name = 'post'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['forms'] = CommentForm()
#         return context
#
#
# class CommentCreateView(generic.CreateView):
#     model = CommentPost
#     form_class = CommentForm
#     #
#     # def get_success_url(self):
#     #     return reverse_lazy('detail_post')
#
#     def form_valid(self, form):
#         obj = form.save(commit=False)
#         obj.author = self.request.user
#
#         post_id = int(self.kwargs['post_id'])
#         post = get_object_or_404(Post, id=post_id)
#         obj.post = post
#
#         return super().form_valid(form)
#
#
