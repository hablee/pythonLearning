from first import yolo_detect

pathIn = './test_imgs/test1.jpg'
pathOut = './result_imgs/test1.jpg'
yolo_detect(pathIn,pathOut)

# >>> 从硬盘加载YOLO......
# >>> YOLO模型花费 3.63 秒来预测一张图片

pathIn = './test_imgs/test2.jpg'
pathOut = './result_imgs/test2.jpg'
yolo_detect(pathIn,pathOut)
# >>> 从硬盘加载YOLO......
# >>> YOLO模型花费 3.55 秒来预测一张图片

# pathIn = './test_imgs/test3.jpg'
# pathOut = './result_imgs/test3.jpg'
# yolo_detect(pathIn,pathOut)
# >>> 从硬盘加载YOLO......
# >>> YOLO模型花费 3.75 秒来预测一张图片