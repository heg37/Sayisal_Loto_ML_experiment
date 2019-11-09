
"""---------------------------------------------------------------------"""
"""                                                                     """
"""  Train and preparation phases codes for our loto project            """
"""                                                                     """
"""                   This code file has created by                     """
"""                       Hüseyin Emre Girgin                           """
"""                                                                     """
"""             You can use or change the codes freely                  """
"""                                                                     """
"""---------------------------------------------------------------------"""

"""
Warning from developer:
    
    This code wroted on TensorFlow 2.0.0 
    If you are using still TensorFlow v1, you could get some warnings and errors.
    If you don't have TensorFlow 2.0.0 you can run codes on Colab as like me.
"""

"""-----------------------------------------------------------"""
"""              We are adding our libraries                  """
"""-----------------------------------------------------------"""

import numpy as np
import tensorflow as tf
from __future__ import absolute_import, division, print_function, unicode_literals

"""-------------------------------------"""
"""             Preparation             """
"""-------------------------------------"""

file_name = 'lotodataset3.npz'
with np.load(file_name) as read:
  x_train = read['InputsTrain']
  x_test = read['OutputsTrain']
  y1_traina = np.transpose(read['y1_train'])
  y1_testa = np.transpose(read['y1_test'])
  y2_traina = np.transpose(read['y2_train'])
  y2_testa = np.transpose(read['y2_test'])
  y3_traina = np.transpose(read['y3_train'])
  y3_testa = np.transpose(read['y3_test'])
  y4_traina = np.transpose(read['y4_train'])
  y4_testa = np.transpose(read['y4_test'])
  y5_traina = np.transpose(read['y5_train'])
  y5_testa = np.transpose(read['y5_test'])
  y6_traina = np.transpose(read['y6_train'])
  y6_testa = np.transpose(read['y6_test'])

y1_train = y1_traina[0]
y2_train = y2_traina[0]
y3_train = y3_traina[0]
y4_train = y4_traina[0]
y5_train = y5_traina[0]
y6_train = y6_traina[0]

y1_test = y1_testa[0]
y2_test = y2_testa[0]
y3_test = y3_testa[0]
y4_test = y4_testa[0]
y5_test = y5_testa[0]
y6_test = y6_testa[0]

"""---------------------------------------------------------------"""
"""         We are creating our train and test datasets           """
"""---------------------------------------------------------------"""

# if you want to train the NN for which number you should change y1_train to another number. eg. for 2nd number, change y1_train to y2_train and y1_test to y2_test
train_dataset = tf.data.Dataset.from_tensor_slices((x_train, y1_train)) # We create train dataset
test_dataset = tf.data.Dataset.from_tensor_slices((x_test, y1_test)) # We create test dataset

batch_size = 32
shuffle_buffer_size = 50

# Shuffle and buffer
train_dataset = train_dataset.shuffle(shuffle_buffer_size).batch(batch_size)
test_dataset = test_dataset.batch(batch_size)

# I define our outputs max number for NN output. !! Don't forget to change y1_train
max1 = np.amax(y1_train)
max1 = np.float64.astype(max1,int) + 1
print("Maximum number in the array: {}".format(max1-1))

"""-------------------------------------"""
"""         let's build our NN          """
"""-------------------------------------"""

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(2, 2)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(max1, activation='softmax')
])

model.compile(optimizer=tf.keras.optimizers.RMSprop(),
                loss=tf.keras.losses.SparseCategoricalCrossentropy(),
                metrics=[tf.keras.metrics.SparseCategoricalAccuracy()])

"""-------------------------------------"""
"""                Train                """
"""-------------------------------------"""

model.fit(train_dataset, epochs=1000) #you probably want to change 1000 epoch value to lower. You can try 250 but I trained with this value

"""-------------------------------------"""
"""                Test                 """
"""-------------------------------------"""

loss, accuracy = model.evaluate(test_dataset)
print("Model accuracy: {:5.2f}%".format(100*accuracy)) #print accuracy of test

# If you want to save your model you can activate it
#model.save('loto_model_num1.h5')