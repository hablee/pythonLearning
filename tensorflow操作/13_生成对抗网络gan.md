```python
import glob
import imageio
import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
from tensorflow.keras import layers
import time
from IPython import display
import tensorflow as tf

(train_images,train_labels),(_,_)=tf.keras.datasets.mnist.load_data()
train_images=train_images.reshape(train_images.shape[0],28,28,1).astype('float32')
train_images=(train_images-127.5)/127.5 # 将图片标准化到 [-1, 1] 区间内

BUFFER_SIZE=60000
BATCH_SIZE=256

# 批量化和打乱数据
train_dataset=tf.data.Dataset.from_tensor_slices(train_images).shuffle(BUFFER_SIZE).batch(BATCH_SIZE)

# 生成器
def make_generator_model():
    model=tf.keras.Sequential()
    model.add(layers.Dense(7*7*256,use_bias=False,input_shape=(100,)))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())

    model.add(layers.Reshape((7,7,256)))
    assert model.output_shape==(None,7,7,256) # 注意：batch size 没有限制

    model.add(layers.Conv2DTranspose(128,(5,5),strides=(1,1),padding='same',use_bias=False))
    assert model.output_shape==(None,7,7,128)
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())

    model.add(layers.Conv2DTranspose(64,(5,5),strides=(2,2),padding='same',use_bias=False))
    assert model.output_shape==(None,14,14,64)
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())

    model.add(layers.Conv2DTranspose(1,(5,5),strides=(2,2),padding='same',use_bias=False,activation='tanh'))
    assert model.output_shape==(None,28,28,1)
    return model

# 使用（尚未训练的）生成器创建一张图片。
generator=make_generator_model()
noise=tf.random.normal([1,100])
generated_image=generator(noise,training=False)
plt.imshow(generated_image[0,:,:,0],cmap='gray')
plt.show()

# 判别器。判别器是一个基于 CNN 的图片分类器
def make_discriminator_model():
    model=tf.keras.Sequential()
    model.add(layers.Conv2D(64,(5,5),strides=(2,2),padding='same',
                            input_shape=[28,28,1]))

    model.add(layers.LeakyReLU())
    model.add(layers.Dropout(0.3))

    model.add(layers.Conv2D(128,(5,5),strides=(2,2),padding='same'))
    model.add(layers.LeakyReLU())
    model.add(layers.Dropout(0.3))

    model.add(layers.Flatten())
    model.add(layers.Dense(1))

    return model

'''
使用（尚未训练的）判别器来对图片的真伪进行判断。模型将被训练为为真实图片输出正值，
为伪造图片输出负值。
'''
discriminator=make_discriminator_model()
decision=discriminator(generated_image)
print(decision)

# 定义损失函数和优化器
# 该方法返回计算交叉熵损失的辅助函数
cross_entropy=tf.keras.losses.BinaryCrossentropy(from_logits=True)
'''
判别器损失。该方法量化判别器从判断真伪图片的能力。
'''
def discriminator_loss(real_output,fake_output):
    real_loss=cross_entropy(tf.ones_like(real_output),real_output)
    fake_loss=cross_entropy(tf.zeros_like(fake_output),fake_output)
    total_loss=real_loss+fake_loss
    return total_loss

def generator_loss(fake_output):
    return cross_entropy(tf.ones_like(fake_output),fake_output)

generator_optimizer=tf.keras.optimizers.Adam(1e-4)
discriminator_optimizer=tf.keras.optimizers.Adam(1e-4)

checkpoint_dir='./training_checkpoints'
checkpoint_prefix=os.path.join(checkpoint_dir,'ckpt')
checkpoint=tf.train.Checkpoint(generator_optimizer=generator_optimizer,
                               discriminator_optimizer=discriminator_optimizer,
                               generator=generator,
                               discriminator=discriminator)

# 定义训练循环
EPOCHS=50
noise_dim=100
num_examples_to_generate=16
# 我们将重复使用该种子（因此在动画 GIF 中更容易可视化进度）
seed=tf.random.normal([num_examples_to_generate,noise_dim])
# 注意 `tf.function` 的使用
# 该注解使函数被“编译”
@tf.function
def train_step(images):
    noise=tf.random.normal([BATCH_SIZE,noise_dim])
    with tf.GradientTape() as gen_tape,tf.GradientTape() as disc_tape:
        generated_images=generator(noise,training=True)
        real_output=discriminator(images,training=True)
        fake_output=discriminator(generated_images,training=True)
        gen_loss=generator_loss(fake_output)
        disc_loss=discriminator_loss(real_output,fake_output)

    gradients_of_generator=gen_tape.gradient(gen_loss,generator.trainable_variables)
    gradients_of_discriminator=disc_tape.gradient(disc_loss,discriminator.trainable_variables)

    generator_optimizer.apply_gradients(zip(gradients_of_generator,generator.trainable_variables))
    discriminator_optimizer.apply_gradients(zip(gradients_of_discriminator,discriminator.trainable_variables))

def train(dataset,epochs):
    for epoch in range(epochs):
        start=time.time()

        for image_batch in dataset:
            train_step(image_batch)

        # 继续进行时为 GIF 生成图像
        display.clear_output(wait=True)
        generate_and_save_images(generator,epoch+1,seed)

        # 每 15 个 epoch 保存一次模型
        if (epochs+1)%15==0:
            checkpoint.save(file_prefix=checkpoint_prefix)
        print('Time for epoch {} is {} sec'.format(epoch+1,time.time()-start))
    # 最后一个 epoch 结束后生成图片
    display.clear_output(wait=True)
    generate_and_save_images(generator,epochs,seed)

# 生成与保存图片
def generate_and_save_images(model,epoch,test_input):
    # 注意 training` 设定为 False
    # 因此，所有层都在推理模式下运行（batchnorm）。
    predictions=model(test_input,training=False)
    fig=plt.figure(figsize=(4,4))

    for i in range(predictions.shape[0]):
        plt.subplot(4,4,i+1)
        plt.imshow(predictions[i,:,:,0]*127.5+127.5,cmap='gray')
        plt.axis('off')

    plt.savefig('image_at_epoch_{:04d}.png'.format(epoch))
    plt.show()

# 训练
train(train_dataset,EPOCHS)

# 恢复新的检查点
checkpoint.restore(tf.train.latest_checkpoint(checkpoint_dir))

# 创建 GIF
# 使用 epoch 数生成单张图片
def display_image(epoch_no):
    return PIL.Image.open('image_at_epoch_{:04d}.png'.format(epoch_no))

display_image(EPOCHS)

# 使用训练过程中生成的图片通过 imageio 生成动态 gif
anim_file='dcgan.gif'
with imageio.get_writer(anim_file,mode='I') as writer:
    filenames=glob.glob('image*.png')
    filenames=sorted(filenames)
    last=-1
    for i,filename in enumerate(filenames):
        frame=2*(i**0.5)
        if round(frame)>round(last):
            last=frame
        else:
            continue
        image=imageio.imread(filename)
        writer.append_data(image)
    image=imageio.imread(filename)
    writer.append_data(image)

import IPython
if IPython.version_info>(6,2,0,''):
    display.Image(filename=anim_file)
```
