from django.test import TestCase, Client
from blog.models import Post
from django.contrib.auth.models import User
from django.urls import reverse
from blog.forms import EmailPostForm,CommentForm



class ModelMixinTestCase(TestCase):
    def setUp(self):

        self.client = Client()
        self.test_user=User.objects.create_user(
            username= "kaaviya",
            password="123",
            )   
        self.published_queryset = Post.published.all()

        self.draft_post= Post.objects.create(
            title='description',
            author=self.test_user,
            body='hi i am kaaviya',
            status="draft"
        )
        self.published_post = Post.objects.create(
            title="Test post thats status=published",
            author=self.test_user,
            body="This post is created by testuser author",
            slug="post-created-testuser-author",
            status="published",
        )
          
        self.list_url = reverse("blog:post_list")
        self.post_detail_url = reverse(
            "blog:post_detail", args=[
                self.published_post.publish.year,
                self.published_post.publish.month,
                self.published_post.publish.day,
                self.published_post.slug]
        )

        self.form = EmailPostForm(
            data={
                "name": "Kaaviya Elango",
                "email": "neomaddy104@gmail.com",
                "to": "kaaviyaelango21@gmail.com",
                "comments": "Read it!!",
            }
        )

        self.post_share_url=reverse(
            "blog:post_share", args=[2]
                
        )

        self.form = CommentForm(
            data={
                "post": self.published_post,
                "name": "First comment",
                "email": "kaaviyaelango21@gmail.com",
                "body": "Good",
            }
        )

        self.add_tag =self.published_post.tags.add('test')
        self.tag = self.published_post.tags.first()

        self.post_list_by_tag = reverse("blog:post_list_by_tag",args=[self.tag.slug])

        