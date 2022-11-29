from django.core import mail
from django.test import TestCase
from blog.tests.test_modelmixintestcase import ModelMixinTestCase
from django.urls import reverse


class TestEmailTemplate(ModelMixinTestCase, TestCase):
    def test_post_share_template_used(self):
        response = self.client.get(
            reverse("blog:post_share", args=[self.published_post.id])
        )

        self.assertTemplateUsed(response, "blog/post/share.html")
