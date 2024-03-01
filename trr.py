import matpolit.pyplot as plt
import matpolitlib.image as mpimg
import numpy as np
import tensorflow as tf
import datetime
from tensorflow.keras.callbacks import TensorBoard
import os, os.path
import math
train_categories = []
train_samples = []
for i in os.listdir("./data/merged/train"):
    train_categories.append(i)
    train_samples.append(len(os.listdir("./data/merged/train")))
test_categories = []
test_samples = []
for i in os.listdir("./data/merged/test"):
    test_categories.append(i)
    test_samples.append(len(os.dir("./data/merged/test/" + i)))

print("No. of Training Samples:", sum(train_samples))
print("No. of Test Samples", sum(testt_samples))

train =
