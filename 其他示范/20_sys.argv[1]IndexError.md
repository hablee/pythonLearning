创建一个py文件
```python
import sys
import cv2
import numpy as np
# 加载并显示图像
input_file = sys.argv[1]
img = cv2.imread(input_file)
cv2.imshow('2.jpg',img)
cv2.waitKey()
```
在PyCharm的`run`下报错：
```python
Traceback (most recent call last):
  File "D:/pythonLean/test/test1.py", line 5, in <module>
    input_file = sys.argv[1]
IndexError: list index out of range

Process finished with exit code 1
```
sys.argv[]是从`Terminal`的方式打开终端中运行py文件传递的参数，在终端下运行：
```python
python test1.py 2.jpg
```
运行成功，成功显示图片`2.jpg`
