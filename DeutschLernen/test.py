from django.test import TestCase

class DeutschLernenTest(TestCase):
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
