from django.test import TestCase, Client
from blog.models import Post
from django.contrib.auth.models import User
from django.urls import reverse
from blog.tests.test_ModelMixinTestCase import ModelMixinTestCase


class Test_listViews(ModelMixinTestCase,TestCase):

    def test_post_list_GET(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post/list.html")

class Test_DetailViews(ModelMixinTestCase,TestCase):


    def test_post_detail_template_used(self):
        response = self.client.get(self.post_detail_url)
        
        self.assertEqual(200, response.status_code)
        self.assertEqual(
            Post.objects.first().title, "Test post thats status=published"
        )

        self.assertTemplateUsed(response, "blog/post/detail.html")

    

    def test_post_detail_should_return_404_for_invalid_post(self):

        incorrect_year = "2093"
        incorrect_month = "12"
        incorrect_day = "7"
        incorrect_slug = "incorrect_slug"

        incorrect_post_detail_url  = reverse(
            "blog:post_detail", args=[
                 incorrect_year,
                 incorrect_month,
                 incorrect_day,
                 incorrect_slug
                 ]
        )
        unsuccessful_response = self.client.get(incorrect_post_detail_url)

        self.assertEqual(404, unsuccessful_response.status_code)