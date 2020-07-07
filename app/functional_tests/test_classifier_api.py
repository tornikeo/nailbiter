from functional_tests.base import FunctionalTestCase, Utils
import os
import glob
import json
import numpy as np

class ClassifierTests(FunctionalTestCase):
    def test_user_can_get_image_classification(self):
        #User lists his/her files
        this_dir = os.path.dirname(os.path.abspath(__file__))
        image_dir = os.path.join(this_dir, 'sample_images')
        positive_img_dir = os.path.join(image_dir, 'positive')
        negative_img_dir = os.path.join(image_dir, 'negative')
        positive_images = glob.glob(os.path.join(positive_img_dir,'*.jpg'))
        negative_images = glob.glob(os.path.join(negative_img_dir,'*.jpg'))

        #User creates a json request with first positive image
        image = Utils.read_img_to_array(positive_images[0])
        
        # User sends the request
        request = {
            'image': image.tolist()
        }
        response = self.client.get('/image_classifier', 
            data = request
        ).json()

        # Status must be OK
        self.assertEquals(response['status'].lower(), 'ok')

        # Prediction must be an array
        self.assertIsInstance(response['prediction'], list)


