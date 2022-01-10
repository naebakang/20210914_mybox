# File encoding: UTF-8

import matplotlib.pyplot as plt
import os
import re
import shutil
import string
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import losses

print(tf.__version__)

dir_project = r'D:\20200619_research_data\20220107_tutorial_tensorflow'

#
url = "https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"

fname = r'{}\aclImdb_v1'.format(dir_project)
# dataset = tf.keras.utils.get_file(fname, url,
#                                   untar=True, cache_dir=dir_project,
#                                   cache_subdir='')
dataset = r'D:\20200619_research_data\20220107_tutorial_tensorflow/'

dataset_dir = os.path.join(os.path.dirname(dataset), 'aclImdb')

os.listdir(dataset_dir)

#
train_dir = os.path.join(dataset_dir, 'train')
os.listdir(train_dir)

#
sample_file = os.path.join(train_dir, 'pos/1181_9.txt')
with open(sample_file) as f:
    print(f.read())

#
# remove_dir = os.path.join(train_dir, 'unsup')
# shutil.rmtree(remove_dir)

# tensorflow 2.4.0 에서는 진행 불가능.
