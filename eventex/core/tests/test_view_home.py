from django.test import TestCase


class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')


    def test_get(self):
        """get/must return status code 200"""
        #response = self.client.get('/')
        self.assertEqual(200, self.response.status_code)
        #self.assertTemplateUsed(response, 'index.html')


    def test_template(self):
        """must use index.html"""
        #response = self.client.get('/')
        self.assertTemplateUsed(self.response, 'index.html')


    def test_subscription_link(self):
        self.assertContains(self.response, 'href="/inscricao/"')