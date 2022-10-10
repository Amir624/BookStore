from .models import Post,CommentPost


def post_star(request):
    return {'stars': Post.objects.filter(is_star=True)}
