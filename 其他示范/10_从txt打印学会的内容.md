在文本编辑器中新建一个文件，写几句话来总结一下你至
此学到的 Python 知识，其中每一行都以“In Python you can”打头。将这个文件命名为
learning_python.txt，并将其存储到为完成本章练习而编写的程序所在的目录中。编写一
个程序，它读取这个文件，并将你所写的内容打印三次：第一次打印时读取整个文件；
第二次打印时遍历文件对象；第三次打印时将各行存储在一个列表中，再在 with 代码
块外打印它们。
# 代码
```python
filename = 'leaning_python.txt'

with open(filename,encoding='utf-8') as file_object:
    contents = file_object.read()
    print("第一次打印读取整个文件：")
    print(contents)

with open(filename,encoding='utf-8') as file_object:
    print("\n第二次遍历文件对象：")
    for line in file_object:
        print(line.rstrip())
        
with open(filename,encoding='utf-8') as file_object:
    lines = file_object.readlines()#存储到一个列表中

print("\n第三次存储在列表中打印：")
for line in lines:
    print(line.rstrip())
```
# 输出
```python
第一次打印读取整个文件：
在python中，你学会了列表
在python中，你学会了字典
在python中，你学会了函数
在python中，你学会了循环
在python中，你学会了判断
在python中，你学会了文本文件

第二次遍历文件对象：
在python中，你学会了列表
在python中，你学会了字典
在python中，你学会了函数
在python中，你学会了循环
在python中，你学会了判断
在python中，你学会了文本文件

第三次存储在列表中打印：
在python中，你学会了列表
在python中，你学会了字典
在python中，你学会了函数
在python中，你学会了循环
在python中，你学会了判断
在python中，你学会了文本文件
```
