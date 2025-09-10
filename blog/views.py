from django.shortcuts import render
from django.utils import timezone
from blog.models import Post

def index(req):
    posts = Post.objects.filter(published_at__lte=timezone.now())
    return render(req, 'blog/index.html', {"posts": posts})
