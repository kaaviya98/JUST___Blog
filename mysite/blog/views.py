from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post


def paginate(queryset, page, per_page):
    paginator = Paginator(queryset, per_page)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return posts


def post_list(request):

    posts = paginate(Post.published.all(), request.GET.get("page"), 3)

    return render(
        request,
        "blog/post/list.html",
        {"page": request.GET.get("page"), "posts": posts},
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
