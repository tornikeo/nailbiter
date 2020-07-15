from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class HomepageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get(reverse('homepage'))
        self.assertTemplateUsed(response, 'homepage.html')
        

