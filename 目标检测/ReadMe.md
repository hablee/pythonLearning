以下展示项目文件目录。IDE:pycharm，项目名称：kuang

# 一级目录kuang
## 二级目录cfg
### 三级目录coco.names
### 三级目录yolov3.cfg
### 三级目录yolov3.weights(太大了，无法上传,可以到[这里](https://pjreddie.com/media/files/yolov3.weights)下载)
## 二级目录result_imgs
## 二级目录test_imgs
### 三级目录test1.jpg
### 三级目录test2.jpg
## 二级目录first.py
## 二级目录predict.py

解释：`cfg`下的三个文件是yolo的模型参数；`result_imgs`是存储程序运行的结果；`test_imgs`存放要测试的图片；`first.py`是yolov3目标检测函数；`predict.py`是主程序，
输入待测试图片路径和确定输出图片路径。
