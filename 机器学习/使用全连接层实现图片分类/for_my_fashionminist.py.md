```python
import tensorflow as tf
import os
import matplotlib.pyplot as plt

#==================导入数据集
f = tf.keras.datasets.fashion_mnist
(train_x,train_y),(test_x,test_y)=f.load_data()
# print(train_x.shape) 6000*28*28

#==================模型配置
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(), #===将数据拉直为一维数据
    tf.keras.layers.Dense(128,activation='relu'), # 全连接层，激活函数
    tf.keras.layers.Dense(10,activation='softmax'), # 全连接输出层，输出10个类别
])

#===================模型编译
model.compile(optimizer='adam',loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
              metrics=['sparse_categorical_accuracy'])
            #===优化器、损失函数、显示准确率的形式为数字-百分比

#===================设置模型存取位置
checkpoint_save_path = './modelsavepath/fashionminst.ckpt'
if os.path.exists(checkpoint_save_path+'.index'):
    print('=====================load model==============')
    model.load_weights(checkpoint_save_path)

cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_save_path,
                                                 save_weights_only=True,
                                                 save_best_only=True)

#===================模型训练
history = model.fit(train_x,train_y,batch_size=32,epochs=5,
                    validation_data=(test_x,test_y),
                    validation_freq=1,
                    callbacks=[cp_callback])
model.summary() # 28*28 × 256(全连接层) + 256(偏置) + 256*10(全连接层) + 10

#===================可视化训练结果
acc = history.history['sparse_categorical_accuracy']
val_acc = history.history['val_sparse_categorical_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

plt.figure()
plt.plot(acc,label='Training Accuracy')
plt.plot(val_acc,label='Validation Accuracy')
plt.legend()
plt.show()

plt.figure()
plt.plot(loss,label='Training Loss')
plt.plot(val_loss,label='Validation Loss')
plt.legend()
plt.show()
```
