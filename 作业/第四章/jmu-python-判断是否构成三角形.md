输入三角形的三边，判断是否能构成三角形。若能构成输出yes，否则输出no。
# 输入格式:
在一行中直接输入3个整数，3个整数之间各用一个空格间隔，没有其他任何附加字符。
# 输出格式:
直接输出yes或no，没有其他任何附加字符。
# 输入样例1:
`3 4 5`
# 输出样例1:
`yes`
# 输入样例2:
`1 2 3`
# 输出样例2:
`no`
# 解答
```python
x,y,z = input().split(' ')
x = int(x)
y = int(y)
z = int(z)
if x<=0 or y<=0 or z<=0:
        print('no')
elif x+y>z and x+z>y and y+z>x:
        print('yes')
else:
        print('no')                
```
# 测试结果
答案正确
# 思路
首先判断是否三边都大于0，再判断是否符合三角形的条件
