from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K
from keras import optimizers, regularizers
from keras.callbacks import ModelCheckpoint

import matplotlib.pyplot as plt
import numpy as np

from IPython.display import SVG
from keras.utils.vis_utils import model_to_dot

from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc
import tensorflow as tf

print("Hola IA")