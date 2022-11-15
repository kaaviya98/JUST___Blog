from django.test import TestCase
from django.urls import reverse
from blog.tests.test_modelmixintestcase import ModelMixinTestCase


class ListView(ModelMixinTestCase, TestCase):
    def test_post_list_GET(self):
        response = self.client.get(self.post_list_url)

        self.assertTemplateUsed(response, "blog/post/list.html")


class DetailView(ModelMixinTestCase, TestCase):
    def test_post_detail_template_used(self):
        response = self.client.get(self.post_detail_url)

        self.assertTemplateUsed(response, "blog/post/detail.html")

    def test_post_detail_should_return_404_for_invalid_post(self):

        incorrect_year = "2093"
        incorrect_month = "12"
        incorrect_day = "7"
        incorrect_slug = "incorrect_slug"

        incorrect_post_detail_url = reverse(
            "blog:post_detail",
            args=[
                incorrect_year,
                incorrect_month,
                incorrect_day,
                incorrect_slug,
            ],
        )
        response = self.client.get(incorrect_post_detail_url)

        self.assertEqual(404, response.status_code)
