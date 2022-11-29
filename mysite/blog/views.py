from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, FormView
from .models import Post
from .forms import EmailPostForm
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 3
    template_name = "blog/post/list.html"


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


class PostShareView(SuccessMessageMixin, FormView):
    form_class = EmailPostForm
    template_name = "blog/post/share.html"
    success_url = reverse_lazy("blog:post_list")
    success_message = "mail sent"

    def setup(self, request, post_id, *args, **kwargs):
        if hasattr(self, "get") and not hasattr(self, "head"):
            self.head = self.get
        self.request = request
        self.args = args

        post = get_object_or_404(Post, id=post_id, status="published")
        self.kwargs = {"post": post}

    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id, status="published")
        return render(
            request,
            self.template_name,
            {"post": post, "form": EmailPostForm},
        )

    def form_valid(self, form):
        self.send_mail(form.cleaned_data)
        return super(PostShareView, self).form_valid(form)

    def send_mail(self, valid_data):
        post = self.kwargs["post"]
        post_url = self.request.build_absolute_uri(post.get_absolute_url())
        send_mail(
            message=f"Read {post.title} at { post_url }\n\n"
            f"{valid_data['from_name']}'s message: {valid_data['share_message']}",
            from_email=valid_data["from_email"],
            subject=f"{valid_data['from_name']} recommends you read {post.title}",
            recipient_list=[valid_data["to_email"]],
        )
