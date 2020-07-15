from django.test import LiveServerTestCase
from selenium import webdriver
import os
import cv2
import numpy as np


class Utils:
    @staticmethod
    def read_img_to_array(filepath, size=(64,64), gray=True):
        image = cv2.imread(filepath)
        image = cv2.resize(image, size)
        if gray:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            image = np.repeat(image[:,:,np.newaxis],3,axis=-1)

        # print(image.shape)
        return image

MAX_WAIT = 10

class FunctionalTestCase(LiveServerTestCase):
    pass

class FunctionalBrowserTestCase(FunctionalTestCase):
    def setUp(self):
        options = webdriver.firefox.options.Options()
        options.headless = True
        self.browser = webdriver.Firefox(options=options)
        staging_server = os.environ.get("STAGING_SERVER")
        if staging_server:
            self.live_server_url = "http://" + staging_server

    def tearDown(self):
        self.browser.quit()
    
    def wait_for(self, fn):
        start_time = time.time()
        while True:
            try:
                return fn()
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(.5)