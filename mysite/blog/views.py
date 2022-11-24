from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 3
    template_name = "blog/post/list.html"

    def paginate(self, queryset, page, per_page):
        paginator = Paginator(queryset, per_page)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        return posts

    def get(self, request):
        posts = self.paginate(Post.published.all(), request.GET.get("page"), 3)

        return render(
            request,
            self.template_name,
            {"posts": posts, "page": request.GET.get("paginate_by", 3)},
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
