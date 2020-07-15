from functional_tests.base import FunctionalBrowserTestCase

class NewVisitorTest(FunctionalBrowserTestCase):
    def test_can_start_using_homepage(self):
        # User goes to check out our site
        self.browser.get(self.live_server_url)

        # The title is there
        self.assertIn("nail", self.browser.title.lower())

        # There is a distinct header
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('nail', header_text.lower())
        
