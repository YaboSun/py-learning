from sklearn.model_selection import train_test_split
import pandas as pd
import tensorflow as tf
import tensorflow_hub as hub
from datetime import datetime
import bert
from bert import run_classifier
from bert import optimization
from bert import tokenization

# Set the output directory for saving model file
# Optionally, set a GCP bucket location

print(tf.__version__)

# OUTPUT_DIR = "/OUTPUT_DIR"  # @param {type:"string"}
# tf.gfile.MkDir(OUTPUT_DIR)
#
# print('***** Model output directory: {} *****'.format(OUTPUT_DIR))
