#计算三角形面积
import math
a = int(input())
b = int(input())
c = int(input())
s = (a+b+c)/2
# '*'表示乘法，math.sqrt表示开根号
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("三角形边长: ",a,b,c,end=" ")
print("三角形面积: ",area)
