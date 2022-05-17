from django.shortcuts import render
from django.core.paginator import Paginator
from .models import PostModel


def home(request):
    posts = PostModel.post_objects.select_related('author').select_related('category').all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'posts/home.html', {
        'posts': page_obj,
    })


def post_detail(request, slug):
    post = PostModel.objects.filter(slug=slug)\
        .select_related('author')\
        .select_related('category')\
        .first()
    return render(request, 'posts/post-detail.html', {
        'post': post
    })
