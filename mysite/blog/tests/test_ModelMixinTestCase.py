from django.test import TestCase
from blog.models import Post
from django.contrib.auth.models import User


class ModelMixinTestCase(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(
            username= "kaaviya",
            password="123",
            )   

        self.test_post_object_draft= Post.objects.create(
            title='description',
            author=self.test_user,
            body='hi i am kaaviya',
            status='draft'
        )
        self.test_post_object_published= Post.objects.create(
            title='testing title',
            author=self.test_user,
            body='hi i am Madhu',
            status='published'
        )