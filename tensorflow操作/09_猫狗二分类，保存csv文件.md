# 简单说明
`first.py`进行训练，保存模型；`predict.py`进行预测
- 划分数据集
- 文件夹作为标签
- 查看acc和loss曲线图
- 保存模型
- 单独文件导入模型进行预测
- 批量对文件夹中的文件进行预测
- 批量预测的结果保存到支持中文格式的csv的文件中
# first.py
```python
import os
import zipfile
import random
import tensorflow as tf
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from shutil import copyfile
import wget

# 下载数据
# url='https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_3367a.zip'
# file_name=wget.filename_from_url(url=url)
# print(url)
# file_name=wget.download(url)
# print(file_name)

# 解压文件
# local_zip='kagglecatsanddogs_3367a.zip'
# zip_ref=zipfile.ZipFile(local_zip,'r')
# zip_ref.extractall('kagglecatsanddogs_3367a')
# zip_ref.close()
# 查看数据集数量
# print(len(os.listdir('./kagglecatsanddogs_3367a/PetImages/Cat')))
# print(len(os.listdir('./kagglecatsanddogs_3367a/PetImages/Dog')))

# 创建目录
# try:
#     os.makedirs('./cats-v-dogs')
#     os.makedirs('./cats-v-dogs/train')
#     os.makedirs('./cats-v-dogs/test')
#     os.makedirs('./cats-v-dogs/train/cats')
#     os.makedirs('./cats-v-dogs/train/dogs')
#     os.makedirs('./cats-v-dogs/test/cats')
#     os.makedirs('./cats-v-dogs/test/dogs')
# except OSError:
#     pass

# 划分数据集的函数
def split_data(SOURCE,TRAINING,TESTING,SPLIT_SIZE):
    files=[]
    for filename in os.listdir(SOURCE):
        file=SOURCE+filename
        if os.path.getsize(file)>0:
            files.append(filename)
        else:
            print(filename+" is zero length, so ignoring.")
    training_length=int(len(files)*SPLIT_SIZE)
    testing_lenght=int(len(files)-training_length)
    shuffled_set=random.sample(files,len(files))
    training_set=shuffled_set[0:training_length]
    testing_set=shuffled_set[-testing_lenght:]

    for filename in training_set:
        this_file=SOURCE+filename
        destination=TRAINING+filename
        copyfile(this_file,destination)

    for filename in testing_set:
        this_file=SOURCE+filename
        destination=TESTING+filename
        copyfile(this_file,destination)



# 划分数据集
# CAT_SOURCE_DIR='./kagglecatsanddogs_3367a/PetImages/Cat/'
# TRAINING_CATS_DIR='./cats-v-dogs/train/cats/'
# TESTING_CATS_DIR='./cats-v-dogs/test/cats/'
# DOG_SOURCE_DIR='./kagglecatsanddogs_3367a/PetImages/Dog/'
# TRAINING_DOGS_DIR='./cats-v-dogs/train/dogs/'
# TESTING_DOGS_DIR='./cats-v-dogs/test/dogs/'
#
# split_size=0.9
# split_data(CAT_SOURCE_DIR,TRAINING_CATS_DIR,TESTING_CATS_DIR,split_size)
# split_data(DOG_SOURCE_DIR,TRAINING_DOGS_DIR,TESTING_DOGS_DIR,split_size)

# 查看数据集情况
# print(len(os.listdir('./cats-v-dogs/train/cats/')))
# print(len(os.listdir('./cats-v-dogs/train/dogs/')))
# print(len(os.listdir('./cats-v-dogs/test/cats/')))
# print(len(os.listdir('./cats-v-dogs/test/dogs/')))

# 模型建立
model=tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32,(3,3),activation='relu',input_shape=(150,150,3)),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(32,(2,2),activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(64,(3,3),activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(64,(3,3),activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512,activation='relu'),
    tf.keras.layers.Dense(1,activation='sigmoid')
])

# 模型编译
model.compile(optimizer=RMSprop(lr=0.001),loss='binary_crossentropy',metrics=['acc'])

# 文件夹标签和数据关联
TRAINING_DIR='./cats-v-dogs/train'
train_datagen=ImageDataGenerator(rescale=1.0/255.)
train_generator=train_datagen.flow_from_directory(TRAINING_DIR,
                                                  batch_size=50,
                                                  class_mode='binary',
                                                  target_size=(150,150))
VALIDATION_DIR='./cats-v-dogs/test'
validation_datagen=ImageDataGenerator(rescale=1.0/255.)
validation_generator=validation_datagen.flow_from_directory(VALIDATION_DIR,
                                                batch_size=50,
                                                class_mode='binary',
                                                target_size=(150,150))

history=model.fit_generator(train_generator,
                            epochs=10,
                            verbose=1,# 显示日志
                            validation_data=validation_generator)

# model.evaluate(validation_generator)

# 画图
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
acc=history.history['acc']
val_acc=history.history['val_acc']
loss=history.history['loss']
val_loss=history.history['val_loss']

epochs=range(len(acc))
plt.plot(epochs,acc,'r',label='training accuracy')
plt.plot(epochs,val_acc,'b',label='validation accuracy')
plt.title('training and validation accuracy')
plt.legend()
plt.figure()
plt.show()

plt.plot(epochs,loss,'r',label='training loss')
plt.plot(epochs,val_loss,'b',label='validation loss')
plt.legend()
plt.figure()
plt.show()

model.save('cat-dog-prediction.h5')

# 预测
import numpy as np
from tensorflow.keras.preprocessing import image

# test_folder='./test-images/'
#
# img_path='./cats-v-dogs/test/dogs/10025.jpg'
# img=image.load_img(path=img_path,target_size=(150,150))
# x=image.img_to_array(img)
# x=np.expand_dims(x,axis=0)
# this_images=np.vstack([x])
# classes=model.predict(this_images,batch_size=10)
# print(classes[0])
# if classes[0]>0.5:
#     print("predict: dog")
# else:
#     print("predict: cat")

```
# predict.py
```python
# 预测图片
import tensorflow as tf

# 导入之前训练好的模型
model=tf.keras.models.load_model('cat-dog-prediction.h5')


import numpy as np
import os
from tensorflow.keras.preprocessing import image

test_folder='./test-images/' # 放置图片的文件夹
files=[]
for filename in os.listdir(test_folder):
    file=test_folder+filename
    if os.path.getsize(file)>0:
        files.append(filename) #把文件名加上去
    else:
        print(filename+" is zero length, so ignoring.")



import pandas as pd
import numpy as np

# 创建一个空的 DataFrame
df = pd.DataFrame(columns=['文件名', '预测结果'])
# print(df)

i=0
for filename in files:
    img_path=test_folder+filename
    img = image.load_img(path=img_path, target_size=(150, 150)) # 跟训练的数据一样
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    this_images = np.vstack([x])
    classes = model.predict(this_images, batch_size=10)
    # print(classes[0])
    if classes[0] > 0.5:
        print(filename,": dog")
        df.loc[i]=[filename,'dog'] # 加入预测结果
    else:
        print(filename,": cat")
        df.loc[i] = [filename, 'cat'] # # 加入预测结果
    i+=1
# print(df)

# 写入csv
df.to_csv('predict_result.csv',index=False,sep=',',encoding='utf_8_sig')
```
