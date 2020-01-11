from django.test import TestCase
import os

class WordEditTest(TestCase):
    def test_get_form(self):
        response = self.client.get('/Word_edit/create_new_word')
        self.assertEqual(response.status_code, 200)
    def test_post_form(self):
        data = {'Stichwort' : 'Abschlussarbeit',
                        'Category' : 'Substantiv',
                        'Genus' :  'die',
                        'unittype'  :  '3',
                        'Anteil' : '1',
                        'isCreated' : '',
                        'wordAddr' :  '/Wort/2.xml',
                        'explanation_1': 'thesis',
                        'translation_1_1': 'He is writing his thesis',
                        'original_1_1': 'Er schreibt gerade an seiner Abschlussarbeit.'
                        }
        response = self.client.post('/Word_edit/create_new_word', data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(os.path.exists('frontend/Wort/2.xml'))