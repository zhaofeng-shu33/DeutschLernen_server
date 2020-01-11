from django.test import TestCase

class WordEditTest(TestCase):
    def test_get_form(self):
        response = self.client.get('/Word_edit/create_new_word')
        self.assertEqual(response.status_code, 200)