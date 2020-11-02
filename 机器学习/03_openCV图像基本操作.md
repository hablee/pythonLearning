使用环境：pycharm；
保存的文件名：test1.py；
当前项目下的图片：2.jpg；
# 显示图像
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
在`Terminal`下键入
```
python test1.py 2.jpg
```
# 裁剪图像
```
import sys
import cv2
import numpy as np
# 加载并显示图像
input_file = sys.argv[1]
img = cv2.imread(input_file)

# 裁剪图像
h, w = img.shape[:2]
start_row, end_row = int(0.21*h),int(0.73*h)
start_col, end_col = int(0.37*w),int(0.92*w)

# 用numpy式的切分方式裁剪图像，并将其展示出来
img_cropped = img[start_row:end_row,start_col:end_col]
cv2.imshow('cropped',img_cropped)

cv2.waitKey()
```
# 调整图像的大小
```python
import sys
import cv2
import numpy as np
# 加载并显示图像
input_file = sys.argv[1]
img = cv2.imread(input_file)
cv2.imshow('2.jpg',img)


# 裁剪图像
h, w = img.shape[:2]
start_row, end_row = int(0.21*h),int(0.73*h)
start_col, end_col = int(0.37*w),int(0.92*w)

# 用numpy式的切分方式裁剪图像，并将其展示出来
#img_cropped = img[start_row:end_row,start_col:end_col]
#cv2.imshow('cropped',img_cropped)

scaling_factor = 1.3
img_scaled = cv2.resize(img,None,fx=scaling_factor,fy=scaling_factor)
interpolation = cv2.INTER_LINEAR
cv2.imshow('Uniform resizing',img_scaled)

cv2.waitKey()
```
# 只在某个维度下调整
```python
import sys
import cv2
import numpy as np
# 加载并显示图像
input_file = sys.argv[1]
img = cv2.imread(input_file)
cv2.imshow('2.jpg',img)


# 裁剪图像
h, w = img.shape[:2]
start_row, end_row = int(0.21*h),int(0.73*h)
start_col, end_col = int(0.37*w),int(0.92*w)

# 用numpy式的切分方式裁剪图像，并将其展示出来
#img_cropped = img[start_row:end_row,start_col:end_col]
#cv2.imshow('cropped',img_cropped)

img_scaled = cv2.resize(img,(250,400),interpolation=cv2.INTER_AREA)
cv2.imshow('skewed resizeing',img_scaled)

cv2.waitKey()
```
# 保存图像
```python
import sys
import cv2
import numpy as np
# 加载并显示图像
input_file = sys.argv[1]
img = cv2.imread(input_file)
cv2.imshow('2.jpg',img)


# 裁剪图像
h, w = img.shape[:2]
start_row, end_row = int(0.21*h),int(0.73*h)
start_col, end_col = int(0.37*w),int(0.92*w)

# 用numpy式的切分方式裁剪图像，并将其展示出来
img_cropped = img[start_row:end_row,start_col:end_col]
cv2.imshow('cropped',img_cropped)

# 调整尺寸
# img_scaled = cv2.resize(img,(250,400),interpolation=cv2.INTER_AREA)
# cv2.imshow('skewed resizeing',img_scaled)

# 保存图像
output_file = input_file[:-4]+'_cropped.jpg'
cv2.imwrite(output_file,img_cropped)

cv2.waitKey()
```


