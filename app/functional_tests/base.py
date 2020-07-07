from django.test import LiveServerTestCase
import PIL.Image as Image
import numpy as np


class Utils:
    @staticmethod
    def read_img_to_array(filepath):
        image = Image.open(filepath)
        im_arr = np.fromstring(image.tobytes(), dtype=np.uint8)
        im_arr = im_arr.reshape((image.size[1], image.size[0], 3))
        return im_arr

class FunctionalTestCase(LiveServerTestCase):
    pass