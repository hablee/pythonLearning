# 题目
    编写一个MNIST分类器，让它可以训练到99%以上的准确率，并且在达到这个准确率时，就通过回调函数停止训练。一些注意事项。

    它应该在小于10个epochs的情况下成功，所以把epochs改成10个也可以，但不能大过10个。
    当它达到99%以上时，应该打印出 "达到99%准确率，所以取消训练！"的字符串。
    如果你添加了任何额外的变量，请确保你使用与类中使用的变量相同的名称。
    
# 代码
```python
import tensorflow as tf

# 回调函数
class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs=None):
        if(logs.get('loss')<0.1):
            print('\n达到99%准确率，所以取消训练！')
            self.model.stop_training=True
callbacks=myCallback()

# 数据集加载
mnist=tf.keras.datasets.mnist
(x_train,y_train),(x_test,y_test)=mnist.load_data()
x_train=x_train/255.0 # 归一化
x_test=x_test/255.0

import matplotlib.pyplot as plt
img0=plt.imshow(x_train[0])
plt.show()

# 模型建立
model=tf.keras.models.Sequential([tf.keras.layers.Flatten(),
                                  tf.keras.layers.Dense(512,activation='relu'),
                                  tf.keras.layers.Dense(256,activation='relu'),
                                  tf.keras.layers.Dense(10,activation='softmax'),
                                  ])
# 模型编译
model.compile(optimizer='sgd',loss='sparse_categorical_crossentropy')

# 模型拟合
model.fit(x_train,y_train,epochs=10,callbacks=[callbacks])

# 模型评估
model.evaluate(x_test,y_test)

classifications=model.predict(x_test)

# 查看第一张图片及其预测的结果
Number0=classifications[0]
print(Number0)
import numpy as np
print(np.argmax(Number0))
```
