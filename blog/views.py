from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.shortcuts import render_to_response, get_object_or_404

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def index(request):
    post_list = Post.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(post_list, 2)
    try:
        posts_page_no = paginator.page(page)
    except PageNotAnInteger:
        posts_page_no = paginator.page(1)
    except EmptyPage:
        posts_page_no = paginator.page(paginator.num_pages)

    return render(request, 'blog/post_list.html', { 'posts': posts_page_no })
