import tensorflow as tf
import tensorflow.keras as keras
import tensorflowjs as tfjs
import os
DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = DIR + '/../export/'
model = keras.models.load_model(MODEL_DIR + '0001')

tfjs.converters.save_keras_model(model, MODEL_DIR+'js_model/')