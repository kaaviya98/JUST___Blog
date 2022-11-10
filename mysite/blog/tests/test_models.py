from blog.tests.test_ModelMixinTestCase import ModelMixinTestCase
from django.test import TestCase


class Test_model_method(ModelMixinTestCase,TestCase):

    def test_absolute_url_in_model(self):
                self.assertEqual(self.post_detail_url, self.published_post.get_absolute_url())

















