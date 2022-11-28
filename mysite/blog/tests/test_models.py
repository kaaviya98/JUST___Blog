from blog.tests.test_modelmixintestcase import ModelMixinTestCase
from django.test import TestCase
from django.urls import reverse
from blog.models import Post


class TestModelMethod(ModelMixinTestCase, TestCase):
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

    def test_get_top_four_similar_posts_returns_None_for_post_without_tag(
        self,
    ):

        self.assertIsNone(self.draft_post.get_top_four_similar_posts().first())

    def test_get_top_four_similar_posts_returns_similar_posts_for_post_with_tag(
        self,
    ):
        published_posts = self.create_published_posts(count=3)
        for post in published_posts:
            post.tags.add("test")
        first_post = published_posts[0]
        second_post = published_posts[1]

        self.assertTrue(second_post in first_post.get_top_four_similar_posts())
