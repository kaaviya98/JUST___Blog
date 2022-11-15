from django.test import TestCase
from blog.models import Post
from django.contrib.auth.models import User
from django.urls import reverse



class ModelMixinTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="kaaviya",
            password="123",

            )   
        self.published_queryset = Post.published.all()

        self.draft_post = Post.objects.create(
            title="description",
            author=self.user,
            body="hi i am kaaviya",
            status="draft",
        )
        self.published_post = Post.objects.create(
            title="testing title",
            author=self.user,
            body='hi i am Madhu',
            status='published',
            slug='testing-title',
        )
        self.post_list_url = reverse("blog:post_list")
        self.post_detail_url = reverse(
            "blog:post_detail",
            args=[
                self.published_post.publish.year,
                self.published_post.publish.month,
                self.published_post.publish.day,
                self.published_post.slug,
            ],
        )
