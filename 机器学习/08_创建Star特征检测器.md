工具：pycharm

保存的文件：test1.py

测试图片：2.jpg

# 代码
```python
import sys
import cv2
import numpy as np

# 定义一个类，用于处理与Star特征检测相关的函数：
class StarFeatureDetector(object):
    def __init__(self):
        self.detector = cv2.xfeatures2d.StarDetector_create()
    # 定义一个对输入图像运行检测器的函数
    def detect(self,img):
        return self.detector.detect(img)

# 在main函数中加载输入图像
if __name__=='__main__':
    # 加载图像
    input_file = sys.argv[1]
    input_img = cv2.imread(input_file)
    # 将图像转为灰度
    img_gray = cv2.cvtColor(input_img,cv2.COLOR_BGR2GRAY)
    # 用Star特征检测器检测出特征
    keypoints = StarFeatureDetector().detect(input_img)
    # 画出输入图像的关键点
    cv2.drawKeypoints(input_img,keypoints,input_img,
                      flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    # 显示输出图像
    cv2.imshow('Star features',input_img)
    cv2.waitKey()
```
