```python
import tensorflow as tf
from tensorflow.keras import layers
from matplotlib import pyplot as plt
import cv2 as cv
from PIL import Image
import numpy as np


image_path = 'D:/pythonLean/train_minist/predictImage/original2.jpg'
image = cv.imread(image_path)


def myaugment_rotate(image):
  """图像增强，旋转"""
  data_augmentation = tf.keras.Sequential([
    layers.experimental.preprocessing.RandomFlip("horizontal_and_vertical"),
    layers.experimental.preprocessing.RandomRotation(0.4),
  ])
  for i in range(10):
    # 增加维度
    result = tf.expand_dims(image, 0)
    # 图像增强
    result = data_augmentation(result)
    # 降维
    result = tf.squeeze(result)
    # 将tf.tesor张量变为array格式才能进行图片保存
    result = np.array(result).astype('uint8')
    # 保存图片
    plt.imsave('D:/pythonLean/train_minist/predictImage/s'+str(i+1)+'.jpg',result)

def myaugment_scale(image):
  """尺寸变换"""
  IMG_SIZE = 300
  resize_and_rescale = tf.keras.Sequential([
    layers.experimental.preprocessing.Resizing(IMG_SIZE, IMG_SIZE),
    layers.experimental.preprocessing.Rescaling(1. / 255)
  ])
  for i in range(5):
    print('original shape:',image.shape)
    result = resize_and_rescale(image)
    print('result shape: ', result.shape)
    # 降维
    result = tf.squeeze(result)
    # # 显示图片
    # plt.imshow(result)
    # plt.show()
    # 将tf.tesor张量变为array格式才能进行图片保存
    result = np.array(result).astype('uint8')
    # 保存图片
    plt.imsave('D:/pythonLean/train_minist/predictImage/s' + str(i + 1) + '.jpg', result)

myaugment_rotate(image)
```
