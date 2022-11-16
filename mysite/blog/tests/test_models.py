from blog.tests.test_ModelMixinTestCase import ModelMixinTestCase
from django.test import TestCase
from django.urls import reverse, resolve


class Test_model_method(ModelMixinTestCase, TestCase):
    def test_absolute_url_in_model(self):
        self.assertEqual(
            reverse(
                "blog:post_detail",
                args=[
                    self.published_post.publish.year,
                    self.published_post.publish.month,
                    self.published_post.publish.day,
                    self.published_post.slug,
                ],
            ),
            self.published_post.get_absolute_url(),
        )
