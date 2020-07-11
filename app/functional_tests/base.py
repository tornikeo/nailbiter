from django.test import LiveServerTestCase
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

class FunctionalTestCase(LiveServerTestCase):
    pass