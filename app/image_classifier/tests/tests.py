from django.test import LiveServerTestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.utils.html import escape
from unittest import skip
import json
from django.test import TestCase
from django.utils.encoding import force_str

from image_classifier.views import get_image_classification

# Create your tests here.
class ClassifierTests(LiveServerTestCase):
    def test_api_call_resolves_to_view(self):
        found = resolve('/image_classifier')
        self.assertEqual(found.func, 
            get_image_classification
        )

    def test_api_call_succeeds(self):
        response = self.client.get('/image_classifier')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            json.loads(force_str(response.content)),
            {'status':'ok'}
        )
