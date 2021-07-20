# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 15:36:54 2021

@author: taebe
"""


# from tensorflow.python.client import device_lib
# device_lib.list_local_devices()


import tensorflow as tf
import tensorflow_datasets as tfds

ds = tfds.load('waymo_open_dataset/v1.0', 
               data_dir='gs://waymo_open_dataset_v_1_0_0_individual_files/tensorflow_datasets')
