首先要引入随机模块`import random`
```python
import random
s1=[1,2,3,4,5,6]
random.shuffle(s1)
print(s1)
random.choice(s1)#随机在s1中取出一个值
```
另外
```python
import random
random.random()#返回0-1之间的浮点数
random.randint(1,100)#返回1-99之间的整数

```
