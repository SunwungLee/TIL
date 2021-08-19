# -*- coding: utf-8 -*-
"""
tfrecord 파일 사용법

@author: S Lee
@date: 2021.07.20
"""

'''
TFRecord

TFRecord는 TensorFlow에서 지원하는 파일 형식이다. 
공식 홈페이지에는 TFRecord에 대해서 
The TFRecord file format is a simple record-oriented binary format 
that many TensorFlow applications use for training data.라고 표현하고 있다. 
간단히 말해서 바이너리 형식으로 저장하기 위한 용도의 파일 형식이라는 의미이다. 
즉, TFRecord는 데이터를 자체적인 바이너리 형식으로 저장하는 기능을 제공한다.

다음은 VCTK 데이터셋을 TFRecord로 변환하여 저장해주는 함수를 구현한 예제이다. 
데이터셋의 형식은 위의 from_generator 예제의 형식과 동일하게 구현하였다

'''

import tensorflow as tf


filenames = 'open_waymo_dataset_1.tfrecord'
raw_dataset = tf.data.TFRecordDataset(filenames)

print(raw_dataset)
# open_waymo_dataset_1.tfrecord