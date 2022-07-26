from django.test import TestCase, Client

# Create your tests here.
class EchoHostnameViewTests(TestCase):
    def test_index(self):
        client = Client()
        response = client.get('/')
        content = response.content.decode('utf-8')
        self.assertTrue('echo-hostname' in content)
