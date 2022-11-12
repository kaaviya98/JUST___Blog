from django.core import mail
from django.test import TestCase
from blog.tests.test_modelmixintestcase import ModelMixinTestCase

class EmailTest(TestCase):
    def test_send_email(self):
        mail.send_mail('Subject here', 'Here is the message.',
            'from@example.com', ['to@example.com'],
            fail_silently=False)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Subject here')
     
class Test_emailTemplate(ModelMixinTestCase, TestCase):
    def test_post_share_template_used(self):
        response = self.client.get(self.post_share_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post/share.html")