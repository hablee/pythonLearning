工具：pycharm

需要安装`pip install opencv-contrib-python`，否则`sift = cv2.cv.xfeatures2d.SIFT_create()`函数会报错

测试图片：2.jpg

保存的文件名：test1.py

# 代码
```python
import sys
import cv2
import numpy as np

# 加载图像
input_file = sys.argv[1]
img = cv2.imread(input_file)

# 将图像转为灰度
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 初始化SIFT检测器对象并提取关键点
sift = cv2.xfeatures2d.SIFT_create()
keypoints = sift.detect(img_gray,None)

# 在图像上画出关键点
img_sift = np.copy(img)
cv2.drawKeypoints(img,keypoints,img_sift,flags=(cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS))

# 显示输入和输出图像
cv2.imshow('input image',img)
cv2.imshow('SIFT features',img_sift)
cv2.waitKey()

cv2.waitKey()
```
在`Terminal`窗口键入：
```python
python test1.py 2.jpg
```
