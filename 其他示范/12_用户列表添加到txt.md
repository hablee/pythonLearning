编写一个 while 循环，提示用户输入其名字。用户输入其名字后，
在屏幕上打印一句问候语，并将一条访问记录添加到文件 guest_book.txt 中。确保这个
文件中的每条记录都独占一行。
# 代码
```python
name = input("请输入您的名字(输入'q'退出，不再输入)：")
while True:
    if name=='q':
        break
    filename = 'guest.txt'
    with open(filename,'a',encoding='utf-8') as file_object:
        file_object.write(name+"\n")
    name = input("请输入您的名字(输入'q'退出，不再输入)：")
```
# 输出
```python
请输入您的名字(输入'q'退出，不再输入)：李海宝
请输入您的名字(输入'q'退出，不再输入)：王婉莹
请输入您的名字(输入'q'退出，不再输入)：李平良
请输入您的名字(输入'q'退出，不再输入)：谌利君
请输入您的名字(输入'q'退出，不再输入)：李淑颖
请输入您的名字(输入'q'退出，不再输入)：李嘉颖
请输入您的名字(输入'q'退出，不再输入)：q
```
