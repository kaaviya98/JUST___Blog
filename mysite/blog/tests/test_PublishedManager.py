from django.test import TestCase
from blog.models import Post
from blog.tests.test_ModelMixinTestCase import ModelMixinTestCase


class Test_Published_Manager(ModelMixinTestCase,TestCase):

   def test_published_manager(self):
            
            objects_queryset_with_status_published = Post.objects.filter(
                status="published"
            )
            self.assertQuerysetEqual(
                self.published_queryset, objects_queryset_with_status_published
            ) 
    