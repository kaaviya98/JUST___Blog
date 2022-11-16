from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post


def paginate(paginator, page):
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return posts


def post_list(request):
    published_post = Post.published.all()
    paginator = Paginator(published_post, 3)
    page = request.GET.get("page")

    posts = paginate(paginator, page)

    return render(
        request, "blog/post/list.html", {"page": page, "posts": posts}
    )


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        slug=post,
        status="published",
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    return render(request, "blog/post/detail.html", {"post": post})
