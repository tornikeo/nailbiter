from django.test import LiveServerTestCase
from django.test.client import 

class ClassifierTests(LiveServerTestCase):
    def test_api_call_succeeds(self):
