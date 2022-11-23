from django.test import TestCase
from blog.models import Post
from django.contrib.auth.models import User


class ModelMixinTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="kaaviya",
            password="123",
        )

        self.draft_post = Post.objects.create(
            title="description",
            author=self.user,
            body="hi i am kaaviya",
            status="draft",
        )
        self.published_post = Post.objects.create(
            title="testing title",
            author=self.user,
            body="hi i am Madhu",
            status="published",
            slug="testing-title",
        )

    def create_published_posts(self, count):
        posts = []
        for _ in range(count):
            post = Post.objects.create(
                title="Published2",
                author=self.user,
                body="Testing Published2",
                status="published",
                slug="published2",
            )
            posts.append(post)
        return posts
