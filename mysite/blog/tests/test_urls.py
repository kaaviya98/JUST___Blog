from django.test import SimpleTestCase
from django.urls import resolve
from blog.views import post_list, post_detail
from blog.tests.test_modelmixintestcase import ModelMixinTestCase


class TestUrls(ModelMixinTestCase, SimpleTestCase):
    def test_post_list_url_is_resolved(self):
        self.assertEquals(resolve(self.post_list_url).func, post_list)

    def test_post_detail_url_is_resolved(self):
        self.assertEquals(resolve(self.post_detail_url).func, post_detail)
