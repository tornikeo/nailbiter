from django.test import LiveServerTestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.utils.html import escape
from unittest import skip
from django.test import TestCase
from django.utils.encoding import force_str
import numpy as np

from image_classifier.views import get_image_classification

# Create your tests here.
class ClassifierTests(LiveServerTestCase):
    def test_api_call_resolves_to_view(self):
        found = resolve('/image_classifier')
        self.assertEqual(found.func, 
            get_image_classification
        )

    def test_api_call_succeeds(self):
        request = np.ones((200, 200, 3), dtype=np.float).tolist()
        response = self.client.get('/image_classifier',
            data={'image':request}
        )
        self.assertEqual(response.status_code, 200)
        
    def test_response_is_well_structured(self):
        request = np.ones((200, 200, 3), dtype=np.float).tolist()
        response = self.client.get('/image_classifier',
            data={'image':request}
        )
        response = response.json()
        for key in ('status', 'prediction'):
            self.assertIn(key,response)
        
        self.assertIsInstance(response['prediction'], list)

        self.assertEqual(len(response['prediction']), 2, 
            f"expected 2 classes in prediction, but got {len(response['prediction'])}"
        )
