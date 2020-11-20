```python
import tensorflow as tf
import PIL.Image as IM
import numpy as np
import os

f = tf.keras.datasets.fashion_mnist
(train_x,train_y),(test_x,test_y)=f.load_data()
#=================表明模型存储的路径
model_save_path = './modelsavepath/fashionminst.ckpt'

#==================按照训练的神经网络进行配置模型
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128),
    tf.keras.layers.Dense(10),
])

#===================导入已存储的模型
model.load_weights(model_save_path)

#===================应用模型进行预测
# 待预测图片路径
images_path = 'D:/pythonLean/train_minist/predictImage/'
filelist = os.listdir(path=images_path) # 该文件夹下所有的文件(包括文件夹)

# 字典
predic_dic={}

for file in filelist:
    thedir = os.path.join(images_path, file)  # 图片文件路径
    img = IM.open(thedir) # 打开文件
    # 使得待预测图片与训练图片大小一致
    img = img.resize((28,28),IM.ANTIALIAS)
    # 转成灰度图
    img_arr = np.array(img.convert('L'))
    # 归一化
    img_arr = img_arr/255.0
    # 增加待测图片的维度
    print('img_arr:',img_arr.shape)
    x_predict = img_arr[tf.newaxis,]
    print('x_predict:',x_predict.shape)
    # 打印预测结果
    result = model.predict(x_predict)
    pred = tf.argmax(result,axis=1)
    predic_num = np.array(pred)[0]
    predic_dic[file]=predic_num

# 通过字典打印结果
for key in predic_dic:
    print(key+": "+str(predic_dic[key]))
```
