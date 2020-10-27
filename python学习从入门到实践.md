# 完整学习笔记
# 第二章：变量和简单数据类型

## 使用title()方法将单词的首字母大写

输入：

```python
first_name = "ada"
last_name = "lovelace"
full_name = first_name+" "+last_name
print("\t"+full_name.title())
```

输出：

```python
	Ada Lovelace#因为前面有\t制表符
```

## 字符串的大小写

输入：

```python
myname = "li hai bao"
NAME = myname.upper()
print(NAME)#输出：LI HAI BAO
name = NAME.lower()
print(name)#输出：li hai bao
```

`lower()`和`upper()`不会改变原来变量的值

## 使用rstrip()方法去除末尾的空格

输入：

```python
test = " python "
print(test)
print(test.rstrip())
```

输出：

```python
 python #这里是有一个空格的
 python
```

如果需要**改变**原来`test`的值，需要将修改后的值保存到变量中，输入：

```python
test="lang  "
test=test.rstrip()
print(test)
```

输出：

```python
lang#无空格
```

## 同理可以使用lstrip()去除字符串开头的空格，使用strip()同时去除字符串两端的空格

```python
test = " lang "
print(test.strip())
```

## python中的加减乘除操作

输入：

```python
2+3
3-2
2*3
3/2
```

对于分别输出：

```py
5
1
6
1.5
```

python使用2个乘号表示**乘方**运算

输入：

```python
3**2
3**3
10**6
```

输出：

```python
9
27
1000000
```

使用**括号**来确定复杂的运算顺序。

## tips：Python shell清屏的方法

- 1.在当前shell下新建文件（file-->new file）
- 2.关闭当前shell
- 3.在新建的文件下，选择Run-->Python Shell

## 使用str()显示地将非字符串值表示为字符串

输入：

```python
age = 23
meg = "Happy "+str(age)+"rd Birthday!"
print(meg)
```

输出：

```python
Happy 23rd Birthday!
```

## 注释

`#`为单行注释

前后的`'''`为多行注释，`'`为单引号

## 第二章总结

- 变量及变量名
- 字符串大小写，首字母大写，去除首尾多余空格
- 整数和浮点数
- 注释

# 第三章：列表

## 列表的表示，方括号：[]

变量名使用**复数**

输入：

```python
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
```

输出：

```python
['trek', 'cannondale', 'redline', 'specialized']
```

## 使用索引访问列表元素

**索引从0开始**

输入：

```python
print(bicycles[1])
```

输出：

```pytho
cannondale
```

**使输出格式更简洁-->**输入：

```python
print(bicycles[1].title())
```

输出：

```py
Cannondale
```

**索引为**`-1`时返回列表的最后一个元素

```python
print(bicycles[-1])#输出：specialized
```

## 小试牛刀

输入：

```python
names = ['李海宝','李平良','谌利君']
for name in names:
    print("你好，"+name+"!")
```

输出：

```python
你好，李海宝!
你好，李平良!
你好，谌利君!
```

## 修改列表的值

输入：

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'hopn'
print(motorcycles)
```

输出：

```python
['hopn', 'yamaha', 'suzuki']
```

## 在列表中添加元素

### 末尾添加使用append

输入：

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('newItem')
print(motorcycles)
```

输出：

```python
['honda', 'yamaha', 'suzuki', 'newItem']
```

可以创建一个`空列表`，然后动态地往里面添加元素

输入：

```python
names = []
names.append('李海宝')
names.append('李平良')
names.append('谌利君')
print(names)
```

输出：

```python
['李海宝', '李平良', '谌利君']
```

### 中间插入用insert(index,item)

输入：

```py
names = ['谌利君','李淑颖']
names.insert(0,'李平良')
print(names)
```

输出：

```py
['李平良', '谌利君', '李淑颖']
```

## 删除元素

### 知道索引，使用del

输入：

```python
names = ['谌利君','李淑颖']
names.insert(0,'李平良')
del names[1]
print(names)
```

输出：

```python
['李平良', '李淑颖']
```

### 使用pop()删除末尾元素，该方法有返回值(意味着可以保存下来使用)

输入：

```python
names = ['谌利君','李淑颖']
names.insert(0,'李平良')
popItem = names.pop()
print(names)
print(popItem)
```

输出：

```python
['李平良', '谌利君']
李淑颖
```

`pop(index)`删除任意位置的元素

输入：

```python
motorcycles = ['honda', 'yamaha', 'suzuki']

popItem = motorcycles.pop(1)
print(motorcycles)
print("the second motorcycle I owned is "+popItem.title())
```

输出：

```python
['honda', 'suzuki']
the second motorcycle I owned is Yamaha
```

### 知道值，用remove()删除

输入：

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
tooExpensive = 'yamaha'

motorcycles.remove(tooExpensive)
print(motorcycles)
print("a "+tooExpensive.title()+" is too expensive")
```

输出：

```python
['honda', 'suzuki']
a Yamaha is too expensive
```

## 列表排序

## sort()按字母顺序永久修改列表顺序

输入：

```python
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
```

输出：

```python
['audi', 'bmw', 'subaru', 'toyota']
```

**sort(reverse=True)使按字母顺序相反的顺序排列，修改也是永久性的**

输入：

```python
cars.sort(reverse=True)
```

输出：

```python
['toyota', 'subaru', 'bmw', 'audi']
```

### sorted() : 按字母顺序临时排序，保留列表原来的顺序

**注意用法**

输入：

```python
cars = ['bmw','audi','toyota','subaru']

print("sorted list: ")
print(sorted(cars))
print("original list: ")
print(cars)
```

输出：

```python
sorted list: 
['audi', 'bmw', 'subaru', 'toyota']
original list: 
['bmw', 'audi', 'toyota', 'subaru']
```

**同样也可以用reverse=True传递参数**反向临时排序：

```python
tempSorted = sorted(cars,reverse=True)
print(tempSorted)
```

## 永久性反转列表：reverse()；注意这不是排序！

输入：

```python
cars = ['bmw','audi','toyota','subaru']

cars.reverse();
print(cars)
```

输出：

```python
['subaru', 'toyota', 'audi', 'bmw']
```

## len()确定列表长度

```python
cars = ['bmw','audi','toyota','subaru']
print(len(cars))#输出4
```

## 第三章总结

- 列表的概念及表示
- 增删元素
- 列表按字母排序，按字母反向排序；永久排序，临时排序
- 反转列表
- 确定列表长度

# 第四章：操作列表

## for循环遍历整个列表

输入：

```python
cars = ['bmw','audi','toyota','subaru']
for car in cars:
    print("I can't wait to see "+car.upper()+" next time!")
    print("thas's amazing!\n")#每次迭代结束之后都插入一个空行
print("Thank you all!")
```

输出：

```python
I can't wait to see BMW next time!
thas's amazing!

I can't wait to see AUDI next time!
thas's amazing!

I can't wait to see TOYOTA next time!
thas's amazing!

I can't wait to see SUBARU next time!
thas's amazing!

Thank you all!
```

## 使用range()创建数字列表，左闭右开区间

### 例子1：

```python
numbers = list(range(1,6))
print(numbers)
```

### 输出1：

```python
[1, 2, 3, 4, 5]
```

### 例子2：

```python
evenNumbers = list(range(2,11,2))
print(evenNumbers)
```

### 输出2：

```python
[2, 4, 6, 8, 10]
```

### 例子3：

```python
squares=[]
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)
```

### 输出3：

```python
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

## 计算数字列表的最大值、最小值、总和

输入：

```python
nums = [1,2,3,4]
print(min(nums))
print(max(nums))
print(sum(nums))
```

输出：

```python
1
4
10
```

## 使用列表解析创建列表

`列表解析`将for循环和创建新元素的代码合并成一行，并自动附加新元素  

对应**使用range()创建数字列表**中的**例子3**：

```python
squares = [value**2 for value in range(1,11)]
print(squares)
```

输出结果是一样的：

```python
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

## 切片操作，左闭右开区间

输入：

```python
players = ['zhao','qian','sun','li']
print(players[1:3])
```

输出的也是一个列表：

```python
['qian', 'sun']
```

如果没有指定起始索引，python自动从列表头开始切片操作；如果没有指定终止索引，python自动切到末尾。

### 负数索引返回离列表末尾相应距离的元素

如：输出名单最后2位的player

```python
players = ['zhao','qian','sun','li']
print(players[-2:])
```

输出：

```python
['sun', 'li']
```

### 遍历切片

如：遍历前2名player：

```python
players = ['zhao','qian','sun','li']
for player in players[:2]:
    print(player.title())

print('遍历结束')
```

输出：

```python
Zhao
Qian
遍历结束
```

### 使用切片复制列表（省略前后索引）

输入：

```python
players = ['zhao','qian','sun','li']
players2 = players[:]

print("players: ")
print(players)
print("\nplayers2: ")
print(players2)
```

输出：

```python
players: 
['zhao', 'qian', 'sun', 'li']

players2: 
['zhao', 'qian', 'sun', 'li']
```

## 不可变的列表：元组

### 定义一个大小不可变的矩形

```python
dimentions = (200,50)#使用圆括号
print(dimentions[0])
print(dimentions[1])
```

输出：

```python
200
50
```

**如果要修改元组，可以重新给元组赋值**

```python
dimentions = (200,50)
print("original: ")
print(dimentions)
dimentions = (100,40)
print("\nmodified: ")
print(dimentions)
```

输出：

```python
original: 
(200, 50)

modified: 
(100, 40)
```

### 遍历元组中的所有值跟列表一样

```python
dimentions = (200,50)
for dimention in dimentions:
    print(dimention)
```

输出：

```python
200
50
```

## 第四章小结

- 创建列表
- 遍历列表
- 切片
- 元组

# 第五章：if语句

条件测试：如果值为True，执行if之后的语句，否则忽略。

```python
cars = ['audi','bmw','subaru','toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
```

输出：

```python
Audi
BMW
Subaru
Toyota
```

## 使用and检查多个条件（同时满足）

```python
age0 = 22
age1 = 18
print(age0 >=21 and age1>=18)#输出：True
```

## 使用or检查多个条件（只需1个满足）

```python
age0 = 22
age1 = 18
print(age0 >=21 or age1>=20)#输出：True
```

## 使用in检查特定值是否包含在列表中

```python
name = ['zhao','qian','sun','li']
if 'li' in name:
    print('李氏在内')
```

输出：

```python
李氏在内
```

使用**not in**检查是否不包含在列表中

```python
name = ['zhao','qian','sun','li']
if 'wang' not in name:
    print('王氏不在内')
```

输出：

```python
王氏不在内
```

## if-elif-else结构

```python
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
    
print("Your admission cost is "+str(price))
```

输出：

```python
Your admission cost is 5 yuan
```

`elif`块可以使用多个，可以不适用`else`块。

## 测试多个条件使用简单if语句

```python
request = ['jin','yin']
if 'jin' in request:
    print("add jin")
if 'tong' in request:
    print("add tong")
if 'yin' in request:
    print("add yin")

print('\nFinished making your request!')
```

输出：

```python
add jin
add yin

Finished making your request!
```

## 使用if语句对列表的操作

```python
requests = []
if requests:#检查列表不空
    for request in requests:
        print("Adding "+request+".")
    print("\nFinished making your requests!")
else:
    print("are you sure you don't request?")
```

输出：

```python
are you sure you don't request?
```

## 在多个列表中使用if语句

```python
available_toppings = ['mushrooms','olives','green peppers',
                      'pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("adding "+requested_topping+".")
    else:
        print("sorry, we don't have "+requested_topping+".")
```

输出：

```python
adding mushrooms.
sorry, we don't have french fries.
adding extra cheese.
```

### 判断用户名是否已被使用

```python
current_users = ['李海宝','高富帅','薛勇','丁老板','邵思阳']
new_users = ['李海宝','丁老板','小师妹','连海鹏']
for new_user in new_users:
    if new_user in current_users:
        print(new_user+"用户名已被使用，请修改！")
    else:
        print(new_user+"用户名未被使用，符合！")
```

输出：

```python
李海宝用户名已被使用，请修改！
丁老板用户名已被使用，请修改！
小师妹用户名未被使用，符合！
连海鹏用户名未被使用，符合！
```

**确保比较不区分大小写，即如果John被注册，应该拒绝用户john的注册**

```python
current_users = ['joHn','micRal','jorDan','wangshIngton']
new_users = ['John','mIcral','shfh','fsakj']
# 将current_users全部转小写
currentUsers = []
for current_user in current_users:
    currentUsers.append(current_user.lower())
#print(currentUsers)
for new_user in new_users:
    if new_user.lower() in currentUsers:
        print(new_user+' have been already registed')
    else:
        print(new_user+' can be regist')
```

## 第五章小结

- if语句
- if-else 语句
- if-elif-else语句，可以没有else
- if、for结合对列表的操作

# 第六章：字典（键值对）

示例：

```python
alien_0 = {'color':'green','points':5}

new_points = alien_0['points']#访问某个键的值
print("You just earned "+str(new_points)+" points!")
```

输出：

```python
You just earned 5 points!
```

## 增加键值对

```python
alien_0 = {'color':'green','points':5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print("\nafter add: ")
print(alien_0)
```

输出：

```python
after add: 
{'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}
```

## 修改值

指定字典名、用方括号`[]`括起的键、以及对于的新值

```python
alien_0 = {'color':'green','points':5}
print(alien_0)

alien_0['color'] = 'yellow'
print("\nafter modified:")
print(alien_0)
```

输出：

```python
{'color': 'green', 'points': 5}

after modified:
{'color': 'yellow', 'points': 5}
```

```python
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: "+str(alien_0['x_position']))

# 向右移动外星人
# 据外星人当前速度决定其将移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 这个外星人的速度一定很快
    x_increment = 3

# 新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x_position: "+ str(alien_0['x_position']))
```

输出：

```python
Original x-position: 0
New x_position: 2
```

## 使用del永久删除键值对

指定要删除的字典名和键，则删除对应的键值对

```python
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(alien_0)
del alien_0['speed']
print("\nafter del:")
print(alien_0)
```

输出：

```python
{'x_position': 0, 'y_position': 25, 'speed': 'medium'}

after del:
{'x_position': 0, 'y_position': 25}
```

## 使用字典创建类似的对象

```python
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'java',
    }
print("sarah's favorite language is "+
      favorite_languages['sarah'].title()+".")
```

输出：

```python
sarah's favorite language is C.
```

**打印一个熟人的信息**

```python
informations = {
    'name':'婉莹',
    'xing':'王',
    'age':'21',
    'city':'Shang hai',
    }
for information in informations:
    print(information+": "+informations[information])
```

输出：

```python
name: 婉莹
xing: 王
age: 21
city: Shang hai
```

## 使用items()遍历字典键和值

```python
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'java',
    }

for name, language in favorite_languages.items():
    print(name.title()+"'s favorite language is "+
          language.title())
```

输出

```python
Jen's favorite language is Python
Sarah's favorite language is C
Edward's favorite language is Ruby
Phil's favorite language is Java
```

## 使用keys()遍历字典的键

```python
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'java',
    }

for name in favorite_languages.keys():
    print(name.title())
```

输出：

```python
Jen
Sarah
Edward
Phil
```

**打印字典中指定的键值**

```python
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'java',
    'yatou':'mysql',
    }

friends = ['sarah','yatou','hablee']
for name in favorite_languages.keys():
    if name in friends:
        print("hi,"+name.title()+"! I see your favorite"+
              " language is "+favorite_languages[name].title())
        
# 如果没有朋友的信息，就打印没有看到
for friend_name in friends:
    if friend_name not in favorite_languages:
        print("I don't see "+friend_name+"'s favorite languages.")
```

输出：

```python
hi,Sarah! I see your favorite language is C
hi,Yatou! I see your favorite language is Mysql
I don't see hablee's favorite languages.
```

### 使用sorted()获得按特定顺序排列的键列表的副本

```python
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'java',
    'yatou':'mysql',
    }
for favoriteKey in sorted(favorite_languages.keys()):
    print(favoriteKey.title())
```

输出：

```python
Edward
Jen
Phil
Sarah
Yatou
```

## 使用values()来遍历字典的值

```python
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'java',
    'yatou':'mysql',
    'else':'python'
    }
print('languages mentioned: \n')
for favoriteValue in set(favorite_languages.values()):
    #使用set()创建不重复的列表(python)
    print(favoriteValue.title())
```

输出：

```python
languages mentioned: 

Java
C
Python
Mysql
Ruby
```

## 存储字典的列表

```python
# 创建一个用于存储外星人的空列表
aliens = []
# 创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

# 显示前5个外星人
for alien in aliens[:5]:
    print(alien)
print("...")
# 显示创建了多少个外星人
print("Total number of aliens: " + str(len(aliens)))
```

输出：

```python
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
...
Total number of aliens: 30
```

## 存储列表的字典

**1个键关联到多个值**，例如：存储所点披萨的信息

```python
pizza = {
    'crust':['thick'],
    'toppings':['mushrooms','extra cheese'],
    }
# 概述所点的披萨
print("You order a pizza with following information:")
cnt = 0
for key in pizza.keys():
    print(key+":")
    for list_item in pizza[key]:
        print(list_item)
    cnt = cnt + 1# 最后一个key不打印空行
    if (cnt)<len(pizza.keys()):
        print()
```

输出：

```python
You order a pizza with following information:
crust:
thick

toppings:
mushrooms
extra cheese
```

喜欢的程序语言可能有多种

```python
favorite_languages = {
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell'],
    }
cnt = 0
for name, languages in favorite_languages.items():
    if cnt!=0:#第一次不打印空行
        print()
    if len(languages)>1:#判断是否喜欢多种程序语言
        print(name.title() + "'s favorite languages are:")
    else:
        print(name.title() + "'s favorite languages is:")
    for language in languages:
        print("\t" + language.title())
    cnt = 1
```

输出：

```python
Jen's favorite languages are:
	Python
	Ruby

Sarah's favorite languages is:
	C

Edward's favorite languages are:
	Ruby
	Go

Phil's favorite languages are:
	Python
	Haskell
```

## 在字典中嵌套字典

```python
users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
        },

    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
        },
    }
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tlocation: " + location.title())
```

输出：

```python
Username: aeinstein
	Full name: Albert Einstein
	location: Princeton

Username: mcurie
	Full name: Marie Curie
	location: Paris
```

## 第六章小结

- 定义字典
- 访问和修改字典键值
- 遍历字典
- 字典与列表的嵌套

# 第七章：用户输入和while循环

## 使用input暂停程序，等待用户输入文本

```python
message = input("please input your name: ")
print(message)
```

输出：

```python
please input your name: hablee#用户输入之后回车
hablee
```

## 使用int接受数值输入

```python
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when "+str(36-height)+" years later!")
```

输出：

```python
How tall are you, in inches? 35#用户输入

You'll be able to ride when 1 years later!
```

## 使用%求余

```python
number = input("input a number, I'll tell you if it's odd: ")
number = int(number)

if number%2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")
```

输出：

```python
input a number, I'll tell you if it's odd: 5#用户输入

The number 5 is odd.
```

## 使用while循环

```python
prompt = "\nTell me something, I will repeat it back to you: "
prompt += "\nInput 'quit' to end the program."

message = ""
while message != 'quit':
    message = input(prompt+"\n:")
    if message != 'quit':
        print(message)
```

输出：

```python
Tell me something, I will repeat it back to you: 
Input 'quit' to end the program.
:quit
```

### 使用break提前结束循环

```python
prompt = "\nPlease input the name of a city you have visited,"
prompt += "\n(input 'quit' when you are finished.)"

while True:
    city = input(prompt+" :")
    if city == 'quit':
        break
    else:
        print("I'd like to go to "+city.title()+".")
```

输出：

```python
Please input the name of a city you have visited,
(input 'quit' when you are finished.) :shanghai
I'd like to go to Shanghai.

Please input the name of a city you have visited,
(input 'quit' when you are finished.) :beijing
I'd like to go to Beijing.

Please input the name of a city you have visited,
(input 'quit' when you are finished.) :xian
I'd like to go to Xian.

Please input the name of a city you have visited,
(input 'quit' when you are finished.) :luoyang
I'd like to go to Luoyang.

Please input the name of a city you have visited,
(input 'quit' when you are finished.) :quit
```

查询票价机器

```python
prompt = "\n此为查询票价机器.\n请输入年龄，输入小于0大于100退出："

while True:
    age = input(prompt)
    age = int(age)
    if age < 0:
        break;
    if age < 3:
        print("\n小于3岁，免费")
    elif age <= 12:
        print("\n3-12岁，票价10元")
    elif age <= 100:
        print("\n超过12岁，票价15元")
    else:
        break
```

输出：

```python
此为查询票价机器.
请输入年龄，输入小于0大于100退出：12

3-12岁，票价10元

此为查询票价机器.
请输入年龄，输入小于0大于100退出：0

小于3岁，免费

此为查询票价机器.
请输入年龄，输入小于0大于100退出：1243
```

**结束本次循环，进入下一次循环用continue**

## 在列表之间移动元素

```python
unconfirmed_users = ['alice','brain','candace']
confirmed_users = []

# 验证每个用户，直到没有未验证用户为止
# 将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
    
# 显示所有已验证的用户
print("\nthe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
```

输出：

```python
Verifying user: Candace
Verifying user: Brain
Verifying user: Alice

the following users have been confirmed:
Candace
Brain
Alice
```

## 删除包含特定值的所有列表元素

```python
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
```

输出：

```python
['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
['dog', 'dog', 'goldfish', 'rabbit']
```

## 使用用户输入来填充字典

```python
responses = {}

# 设置一个标志，指出调查是否继续
polling_active = True

while polling_active:
    # 提示输入被调查者的名字和回答
    name = input("\nWhat is your name? ")#这是Key
    response = input("Which sport would you like? ")#这是value

    # 将答卷存储在字典中
    responses[name] = response

    # 看看是否还有人要参与调查
    repeat = input("would you like to let another person respond?（yes/no）")
    if repeat == 'no':
        polling_active = False

print("\n----- polling results -----")
for name, response in responses.items():
    print(name + " would like " + response + ".")
```

输出：

```python
What is your name? hablee
Which sport would you like? wushu
would you like to let another person respond?（yes/no）yes

What is your name? yuki
Which sport would you like? guita
would you like to let another person respond?（yes/no）no

----- polling results -----
hablee would like wushu.
yuki would like guita.
```

## 第七章小结

- input()
- 文本转数字：int(stringNumber)
- while循环，标志，break，continue
- while操作列表和字典

# 第八章：函数

## 函数的定义

`def`关键字，`()`括号，以`:`结尾

```python
def greet_user():
    '''简单的问候语'''
    name = input("what's your name? ")
    print("hello, "+name)
```

```python
greet_user()
```

输出：

```python
what's your name? hablee#用户输入
hello, hablee
```

## 函数传递参数

```python
def greet_user(user):
    '''简单的问候语'''    
    print("hello, "+user.title())
```

调用：

```python
greet_user('yuki')
```

输出：

```python
hello, Yuki
```

### 位置实参

```python
def describe_pet(animal_type, pet_name):
    '''显示宠物信息'''
    print("\nI have a "+animal_type+".")
    print("my "+animal_type+"'s name is "+pet_name.title()+".")
```

输出：

```python
I have a dog.
my dog's name is None.
```

### 关键字实参

使用关键字实参，务必准确指定函数定义中的形参名

```python
def describe_pet(animal_type, pet_name):
    '''显示宠物信息'''
    print("\nI have a "+animal_type+".")
    print("my "+animal_type+"'s name is "+pet_name.title()+".")

describe_pet('dog','none')
describe_pet(pet_name='none2',animal_type='cat')
```

输出：

```python
I have a dog.
my dog's name is None.

I have a cat.
my cat's name is None2.
```

### 使用默认形参要从后开始放

即先放没有默认值的形参，再放有默认值的实参

```python
def describe_pet(pet_name,animal_type='dog'):
    '''显示宠物信息'''
    print("\nI have a "+animal_type+".")
    print("my "+animal_type+"'s name is "+pet_name.title()+".")

describe_pet('none')
describe_pet(animal_type='cat', pet_name='none2')
```

输出：

```python
I have a dog.
my dog's name is None.

I have a cat.
my cat's name is None2.
```

## 使用return返回函数值

### 让实参变成可选的

```python
def get_formatted_name(first_name, last_name, middle_name = ''):
    '''返回整洁的姓名'''
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name

    return full_name

musician1 = get_formatted_name('li','haibao')
musician2 = get_formatted_name('wu','chengen','targeyen')

print(musician1)
print(musician2)
```

输出：

```python
li haibao
wu targeyen chengen
```

### 返回字典，扩展函数

```python
def build_person(first_name, last_name, age=''):
    '''返回一个字典，其中包含有关一个人的信息'''
    person = {'first':first_name, 'last':last_name}
    if age:# 如果用户输入了年龄，就增加一个键值对
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix','16')
print(musician)
```

输出：

```python
{'first': 'jimi', 'last': 'hendrix', 'age': '16'}
```

### 结合函数和while()循环

```python
def get_formatted_name(first_name, last_name):
    '''返回整洁的姓名'''
    full_name = first_name + ' ' + last_name
    return full_name.title()#将每个单词的首字母大写

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")# 用户可在任何输入的地方选择退出

    f_name = input("first name:")
    if f_name == 'q':
        break

    l_name = input("last name:")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nhello, "+formatted_name + "!")
```

输出：

```python
Please tell me your name:
(enter 'q' at any time to quit)
first name:hab
last name:lee

hello, Hab Lee!

Please tell me your name:
(enter 'q' at any time to quit)
first name:wanying
last name:wang

hello, Wanying Wang!

Please tell me your name:
(enter 'q' at any time to quit)
first name:q
```

## 在函数中修改列表值

```python
def print_models(unprinted_designs, completed_models):
    '''
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    '''
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # 模拟根据设计制作3D打印模型的过程
        print("Printing model: "+current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    '''显示打印好的所有模型'''
    print("\nThe following models hava been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
```

输出：

```python
Printing model: dodecahedron
Printing model: robot pendant
Printing model: iphone case

The following models hava been printed:
dodecahedron
robot pendant
iphone case
```

## 使用切片复制列表的副本，以保留原有列表

```python
print_models(unprinted_designs[:], completed_models)
```

但是这会增加时间和内存的开销。

## 传递任意数量的实参

```python
def make_pizza(*toppings):
    '''打印顾客点的所有配料'''
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("-" + topping)

make_pizza('zhao')
make_pizza('zhao','qian')
```

输出：

```python
Making a pizza with the following toppings:
-zhao

Making a pizza with the following toppings:
-zhao
-qian
```

**如果要使用不同类型的参数，必须在函数定义中将接纳任意数量实参的形参放在最后**

```python
def make_pizza(size, *toppings):
    '''打印顾客点的所有配料'''
    print("\nMaking a "+str(size)+" pizza with the following toppings:")
    for topping in toppings:
        print("-" + topping)

make_pizza(17,'zhao')
make_pizza(4,'zhao','qian')
```

形参名*toppings中的星号让Python创建一个名为toppings的空元组  

输出：

```python
Making a 17 pizza with the following toppings:
-zhao

Making a 4 pizza with the following toppings:
-zhao
-qian
```

### 使用任意数量的关键字实参

使用字典

```python
def build_profile(first, last, **User_info):
    '''创建一个字典，其中包括我们知道的有关用户的一切'''
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last

    for key, value in User_info.items():
        profile[key] = value

    return profile

user = build_profile('albert','einstein',
                     location='princeton',
                     field='physics')
print(user)
```

形参**user_info中的两个星号让Python创建一个名为user_info的空字典，并将收到的所
有名称—值对都封装到这个字典中  

## 将函数存储在模块中

将函数部分存储为一个单独的文件；在当前目录下创建另一个文件，`import`它。

```python
def make_car(manufacture, model, **otherInfo):
    carProfile = {}
    carProfile['manufacture'] = manufacture
    carProfile['model'] = model

    for key, value in otherInfo.items():
        carProfile[key] = value

    return carProfile
```

```python
import first

car = first.make_car('subaru','outback',color='blue',tow_package=True)
print(car)
```

**使用as给模块指定别名**

```python
import first as f
```

### 导入特定的函数

**导入模块中的特定函数：**

`from module_name import function_name`

**导入多个函数：**

`from module_name import function_0, function_1, fuction_2`

```python
from first import make_car

car = make_car('subaru','outback',color='blue',tow_package=True)
print(car)
```

**导入所有函数**

```python
from first import *
```

**使用as给函数指定别名**

```python
from first import make_car as mc
```

## 第八章小结

- 函数定义
- 位置参数、关键字参数、任意参数
- 返回值
- 模块、导入模块、导入模块并命名为别名、导入模块的函数、导入模块的函数并命名为别名

# 第九章：类

## 创建类

```python
class Dog():
    '''一次模拟小狗的简单尝试'''
    def __init__(self, name, age):
        '''初始化属性name和age'''
        self.name = name
        self.age = age

    def sit(self):
        '''模拟小狗被命令时蹲下'''
        print(self.name.title()+" is now sitting.")

    def roll_over(self):
        '''模拟小狗被命令时打滚'''
        print(self.name.title()+" rolled over!")

my_dog = Dog('willie', 6)
print("my dog's name is "+my_dog.name.title()+".")
print("my dog is "+str(my_dog.age)+" years old.")
my_dog.sit()
my_dog.roll_over()
```

**注意：__init__的两边是**2个`_`，不是1个

输出：

```python
my dog's name is Willie.
my dog is 6 years old.
Willie is now sitting.
Willie rolled over!
```

**注意：每个函数都要带上**`self`参数

```python
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("name: "+self.restaurant_name)
        print("type: "+self.cuisine_type)

    def open_restaurant(self):
        print("open state: big open!")

restaurant = Restaurant("hablee's xiaojiuguan", "Yuki")
restaurant.describe_restaurant()
restaurant.open_restaurant()
```

输出：

```python
name: hablee's xiaojiuguan
type: Yuki
open state: big open!
```

## 给属性指定默认值

类中的每个属性都必须有初始值，哪怕这个值是0或空字符串。如果你对某个属性指定了初始值，就无需在`__init__()`中包含为它提供初始值的形参。

```python
class Car():
    '''一次模拟汽车的简单尝试'''
    def __init__(self, make, model, year):
        '''初始化描述汽车的属性'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0 #对属性指定初始值

    def get_descriptive_name(self):
        long_name = str(self.year)+" "+self.make+" "+self.model
        return long_name.title()

    def read_odometer(self):
        '''打印一条指出汽车里程的消息'''
        print("This car has "+str(self.odometer)+" miles in it.")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
```

输出：

```python
2016 Audi A4
This car has 0 miles in it.
```

## 使用方法修改属性的值

```python
class Car():
    '''一次模拟汽车的简单尝试'''
    def __init__(self, make, model, year):
        '''初始化描述汽车的属性'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0 #对属性指定初始值

    def get_descriptive_name(self):
        long_name = str(self.year)+" "+self.make+" "+self.model
        return long_name.title()

    def update_odometer(self, mileage):#更新里程的函数
        '''将里程表读数设置为指定的值'''
        if mileage >= self.odometer:
        	self.odometer = mileage
        else:
            print("Your can't roll back an odometer!")
        
    def read_odometer(self):
        '''打印一条指出汽车里程的消息'''
        print("This car has "+str(self.odometer)+" miles in it.")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(12)#调用更新里程的函数

my_new_car.read_odometer()
```

输出：

```python
2016 Audi A4
This car has 12 miles in it.
```

## 继承

```python
class Car():
    '''一次模拟汽车的简单尝试'''
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' +self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    '''电动汽车的独特之处'''

    def __init__(self, make, model, year):
        '''初始化父类属性'''
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        '''打印一条描述电瓶容量的消息'''
        print("This car has a "+str(self.battery_size)+"-kwh battery.")

my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
```

输出：

```python
2016 Tesla Model S
This car has a 70-kwh battery.
```

### 重写父类的方法

直接重写

```python
def ElectricCar(Car):

    def fill_gas_tank():
        print("电动汽车没有油箱")
```

### 将实类作为属性

```python
class Car():
    '''一次模拟汽车的简单尝试'''
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' +self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():
    '''一次模拟电动汽车电瓶的简单尝试'''
    def __init__(self, battery_size = 70):
        '''初始化电瓶车的属性'''
        self.battery_size = battery_size

    def describe_battery(self):
        '''打印一条描述电瓶容量的消息'''
        print("This car has a "+str(self.battery_size)+"-kwh battery.")

    def get_range(self):
        '''打印一条消息，指出电瓶的续航里程'''
        if self.battery_size == 70:
            orange = 240
        elif self.battery_size == 85:
            orange = 270

        message = "This car can go approximately "+str(orange)
        message += " miles on a full charge."
        print(message)
        

class ElectricCar(Car):
    '''电动汽车的独特之处'''

    def __init__(self, make, model, year):
        '''初始化父类属性'''
        super().__init__(make, model, year)
        self.battery = Battery() #将实例作为属性

my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

my_tesla.battery.get_range()
```

输出：

```python
2016 Tesla Model S
This car has a 70-kwh battery.
This car can go approximately 240 miles on a full charge.
```

## 将类存储在模块中，导入类

### car.py

```python
"""一个可用于表示汽车的类"""

class Car():
    '''一次模拟汽车的简单尝试'''
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性名称"""
        long_name = str(self.year) + ' ' +self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条消息，指出汽车里程"""
        print("This car has "+str(self.odometer_reading)+" miles on it.")

    def update_odometer(self, mileage):
        """
        将里程数设置为指定的值
        拒绝将里程表回拨
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程表读数增加为指定的量"""
        self.odometer_reading += miles
```

### my_car.py

```python
from car import Car

my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
```

输出：

```python
2016 Audi A4
This car has 23 miles on it.
```

## 在一个模块中存储多个类

### car.py

```python
"""一个可用于表示汽车的类"""

class Car():
    '''一次模拟汽车的简单尝试'''
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性名称"""
        long_name = str(self.year) + ' ' +self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条消息，指出汽车里程"""
        print("This car has "+str(self.odometer_reading)+" miles on it.")

    def update_odometer(self, mileage):
        """
        将里程数设置为指定的值
        拒绝将里程表回拨
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程表读数增加为指定的量"""
        self.odometer_reading += miles

class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self, battery_size=70):
        """初始化电瓶车属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a "+str(self.battery_size)+"-kwh battery.")

    def get_range(self):
        """打印一条描述电瓶续航里程的消息"""
        if self.battery_size == 70:
            range_ = 240
        elif self.battery_size == 85:
            range_  = 270

        message = "This car can go approximately "+str(range_)
        message += " miles on a full charge."
        print(message)

class ElectricCar(Car):
    """模拟电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """
        初始化父类的属性，再初始化电动汽车特有的属性
        """
        super.__init__(make, model, year)
        self.battery = Battery()

```

### my_electric_car.py

```python
from car import ElectricCar

my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
```

输出：

```python
2016 Tesla Model S
This car has a 70-kwh battery.
This car can go approximately 240 miles on a full charge.
```

## 从一个模块中导入多个类

```python
from car import Car, ElectricCar
```

## 导入整个模块，使用句点访问需要的类

```python
import car
my_beetle = car.Car('volkswagen', 'beetle', 2016)
my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
```

## 在一个模块中导入另一个模块

比如，在`electric_car.py`中导入`car`模块中的`Car`函数

```python
from car import Car
```

## 从python标准库中导入函数

```python
from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['pjil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is "+
          language.title()+".")
```

输出：

```python
Jen's favorite language is Python.
Sarah's favorite language is C.
Edward's favorite language is Ruby.
Pjil's favorite language is Python.
```

## 类编码风格

- 类名使用`驼峰命名法`，即将类名中每个单词的首字母大写，不使用下划线。实例名和模块名都使用小写，并在单词之间加上下划线。
- 对于每个类，都应紧跟一个文档字符串，简要描述类的功能
- 在类中，使用1个空行来分隔方法；在模块中，使用2个空行来分隔类。

## 第九章小结

- 编写类，属性、方法
- `__init__`函数
- 继承
- 一个类的实例作为另一个类的属性
- 导入模块（文件名），导入模块中的类

# 第十章：文件和异常

## 读取ascii码文件

```python
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
```

`pi_digits.txt`要放在当前文件的目录下

## 使用路径

```python
filename = 'pi_digits.txt' #可以放相对路径或者绝对路径

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())#rstrip()去掉文件每行末尾的换行符
```

## 在with内将每行文件存储到列表中

```python
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    '''readlines()从文件中读取每一行
        并将其存储到1个列表中'''
    
for line in lines:
    print(line.rstrip())
```

## 使用文件的内容

```python
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    '''readlines()从文件中读取每一行
        并将其存储到1个列表中'''
    
pi_string = ''
for line in lines:
    pi_string = pi_string+" "+line.strip()

print(pi_string.strip())
print(len(pi_string))
```

输出：

```python
hablee and yuki and so on
26
```

### 读取中文

```python
filename = 'pi_digits.txt'

with open(filename,encoding='utf-8') as file_object:#使用utf-8编程
    lines = file_object.readlines()
    '''readlines()从文件中读取每一行
        并将其存储到1个列表中'''
    
pi_string = ''
for line in lines:
    pi_string = pi_string+line.strip()

print(pi_string)
```

## 写入文本文件

```python
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming. "+str(100))
```

如果你要写入的文件不存在，函数open()将自动创建它。然而，以写入（ 'w'）模式打开文件时千万要小心，因为如果指定的文件已经存在， Python将在返回文件对象前清空该文件。  

Python只能将字符串写入文本文件。要将数值数据存储到文本文件中，必须先使用函数`str()`将其转换为字符串格式。  

使用`\n`来输出多行

```python
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming. "+str(100)+"\n")
    file_object.write("I love programming2. "+str(100))
```

### 追加文件

使用`'a'`追加已有文件

```python
filename = 'programming.txt'

with open(filename, 'a',encoding='utf-8') as file_object:
    file_object.write("\n追加1")
    file_object.write("\n追加2")
```

## 使用try-except处理异常

```python
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```

输出：

```python
You can't divide by zero!
```

### 依赖于try代码块成功执行的代码都应放到else代码块中

```python
print("Give me two numbers, and I'll dividde them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        ans = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(ans)
```

输出：

```python
Give me two numbers, and I'll dividde them.
Enter 'q' to quit.

First number: 3
Second number: 4
0.75

First number: 6
Second number: 2
3.0

First number: 9
Second number: 0
You can't divide by zero!

First number: q
```

### 文件读取异常

```python
filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "sorry, the file "+filename+" does not exist."
    print(msg)
```

输出：

```python
sorry, the file alice.txt does not exist.
```

### 计算文件中有多少个单词

```python
filename = 'guest.txt'

try:
    with open(filename,encoding='utf-8') as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "sorry, the file "+filename+" does not exist."
    print(msg)
else:
    # 计算文件大致包含多少个字
    words = contents.split()
    num_words = len(words)
    print(filename+" 包含 "+str(num_words)+" 个字.")
```

输出：

```python
guest.txt 包含 6 个字.
```

### 处理多个文件

```python
def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename,encoding='utf-8') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "sorry, the file "+filename+" does not exist."
        print(msg)
    else:
        # 计算文件大致包含多少个字
        words = contents.split()
        num_words = len(words)
        print(filename+" 包含 "+str(num_words)+" 个字.")

filenames = ['alice.txt','siddhartha.txt','moby_dick.txt','little_women.txt']
for filename in filenames:
    count_words(filename)
```

输出：

```python
alice.txt 包含 10 个字.
sorry, the file siddhartha.txt does not exist.
sorry, the file moby_dick.txt does not exist.
sorry, the file little_women.txt does not exist.
```

### 在excep使用pass语句让python什么都不要做

```python
def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename,encoding='utf-8') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        # 计算文件大致包含多少个字
        words = contents.split()
        num_words = len(words)
        print(filename+" 包含 "+str(num_words)+" 个字.")

filenames = ['alice.txt','siddhartha.txt','moby_dick.txt','little_women.txt']
for filename in filenames:
    count_words(filename)
```

输出：

```python
alice.txt 包含 10 个字.
```

## 使用json.dump()存储数据

```python
import json

numbers = [2,3,5,7,11,13]

filename = 'D:\\pythonLean\\numbers.json'
with open(filename,'w') as f_obj:
    json.dump(numbers, f_obj)#2个参数，要存储的数据+文件对象
```

## 使用json.load()读取json文件

```python
import json


filename = 'D:\\pythonLean\\numbers.json'
with open(filename,'r') as f_obj:
    numbers = json.load(f_obj)

print(numbers)
```

## 如果文件存在则打开并输出，否则创建并写入内容

```python
import json

# 如果以前存储了用户名，就加载它
# 否则，就提示用户输入用户名并存储它
filename = 'username1.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:#如果文件不存在
    username = input("what's your name: ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("we'll remember you when you come back, "+username+"!")
else:
    print("welcome back, "+username+"!")

```

输出：

```python
#第一次没有文件时
what's your name: hablee
we'll remember you when you come back, hablee!
#第二次打开程序时
welcome back, hablee!
```

## 重构代码

将代码划分为一系列完成具体工作的函数。这样的过程被称为重构  

```python
import json

def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username1.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """提示输入用户名"""
    username = input("what's your name: ")
    filename = 'username1.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """问候用户,指出其名字"""
    username = get_stored_username()
    if username:
        print("welcome back, "+username+"!")
    else:
        username = get_new_username()
        print("we'll remember you when you come back, "+username+"!")

greet_user()
```

输出：

```python
welcome back, hablee!
```

## 第十章小结

- 文本txt文件的创建、读取
- 一次读取、每行读取、覆盖写入文件、追加写入文件
- try、except、else
- json文件

# 第十一章：测试代码

## name_function.py

```python
def get_formatted_name(first, last):
    """generate a neatly formatted full name"""
    full_name = first + " " + last
    return full_name.title()
```

## test_name_function.py，测试方法

```python
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确处理janis joplin这样的姓名"""
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
        

unittest.main()
```

输出：

```python
.
----------------------------------------------------------------------
Ran 1 test in 0.006s

OK
```

## 测试类

### survey.py

```python
class AnonymousSurvey():
    """收集匿名调查问卷的答案"""

    def __init__(self, question):
        """存储一个问题，并为存储答案做准备"""
        self.question = question
        self.responses = []

    def show_question(self):
        """显示调查问卷"""
        print(self.question)

    def store_response(self, new_response):
        """存储单份调查问卷"""
        self.responses.append(new_response)

    def show_results(self):
        """显示收集到的所有答卷"""
        print("Survey results:")
        for response in self.responses:
            print('-' + response)
```

### test_survey.py

```python
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""
    def test_store_single_response(self):
        question = "what language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')

        self.assertIn('English', my_survey.responses)

    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English','Spanish','Mandarin']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)

unittest.main()
```

### 输出

```python
..
----------------------------------------------------------------------
Ran 2 tests in 0.004s

OK
```

## setUp()方法

unittest.TestCase类包含方法setUp()，让我们只需创建这些对象一次，并在每个测试方法中使用它们。如果你在TestCase类中包含了方法setUp()， Python将先运行它，再运行各个以test_打头的方法。

```python
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""
    def setUp(self):
        """
        创建一个调查对象和一组答案，供使用的测试方法使用
        """
        question = "what language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English','Spanish','Mandarin']
        
    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()
```

输出：

```python
..
----------------------------------------------------------------------
Ran 2 tests in 0.005s

OK
```

## 第十一章小结

- unittest模块
- unittest.TestCase类
- setUp()函数

# 第十二章：武装飞船

## windows安装pygame

- https://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame 安装python版本对应的版本

  例如，我的python版本是3.8,64位操作系统。因此下载：pygame‑1.9.6‑cp38‑cp38‑win_amd64.whl

- 进入到该文件所在路径，如我的在`D:\pythonLean\alien_invasion`

  - C:\Users\a>d:
  - D:\>cd D:\pythonLean\alien_invasion

- 使用pip命令安装：pip install pygame-1.9.6-cp38-cp38-win_amd64.whl

  安装完成显示：Successfully installed pygame-1.9.6

- 输入python，再输入import pygame，可以查看当前安装的pygame版本

## alien_invasion.py

```python
import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_function as gf

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings,screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings,screen,ship,bullets)

if __name__ == '__main__':
    run_game()
```

## bullet.py

```python
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类"""

    def __init__(self,ai_settings,screen,ship):
        """在飞船所处的位置创建一个子弹对象"""
        super(Bullet, self).__init__()
        self.screen = screen

        # 在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储用小数表示的子弹的位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动的子弹"""
        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor
        # 更新表示子弹的rect位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)
```

## game_function.py

```python
import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 向左移动飞船
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
    # 创建一颗子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings,screen,ship,bullets):
    """响应按键和鼠标事件"""
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def update_screen(ai_settings, screen, ship,bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    # 更新子弹位置
    bullets.update()
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
```

## settings.py

```python
class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230,230,230)

        # 飞船的设置
        self.ship_speed_factor = 1.5

        # 子弹设置,宽3像素，高15像素的深灰色子弹
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3
```

## ship.py

```python
import pygame

class Ship():
    def __init__(self,ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            self.center -= self.ai_settings.ship_speed_factor

        # 根据self.center更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)
```

## 第十二章小结

- 安装pygame
- 在屏幕上绘制图像
- 玩家控制游戏元素移动
- 自动移动的元素

# 第十三章：外星人

## alien.py

```python
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人的类"""
    def __init__(self,ai_settings,screen):
        """初始化外星人并设置其起始位置"""
        super(Alien,self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        # 加载外星人图像，并设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image,self.rect)

    def check_edges(self):
        """如果外星人位于屏幕边缘，就返回True"""
        self_rect = self.screen.get_rect()
        if self.rect.right >= self.screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """向右移动外星人"""
        self.x += (self.ai_settings.alien_speed_factor *
                    self.ai_settings.fleet_drop_direction)
        self.rect.x = self.x

```

## alien_invasion.py

```python
import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from ship import Ship
from alien import Alien
import game_function as gf

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    
    pygame.display.set_caption("Alien Invasion")

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 创建一艘飞船
    ship = Ship(ai_settings,screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 创建外星人群
    aliens = Group()
    gf.creat_fleet(ai_settings,screen,ship,aliens)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)

if __name__ == '__main__':
    run_game()
```

## bullet.py

```python
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类"""

    def __init__(self,ai_settings,screen,ship):
        """在飞船所处的位置创建一个子弹对象"""
        super(Bullet, self).__init__()
        self.screen = screen

        # 在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储用小数表示的子弹的位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动的子弹"""
        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor
        # 更新表示子弹的rect位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)
```

## game_function.py

```python
import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def ship_hit(ai_setting,stats,screen,ship,aliens,bullets):
    """响应被外星人撞到的飞船"""
    if stats.ships_left > 0:
        # 将ship_left减1
        stats.ships_left -= 1

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并将飞船放到屏幕底端中央
        creat_fleet(ai_setting,screen,ship,aliens)
        ship.center_ship()

        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 向左移动飞船
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):
    # 创建一颗子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings,screen,ship,bullets):
    """响应按键和鼠标事件"""
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def update_screen(ai_settings, screen, ship,aliens,bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(ai_settings,screen,ship,aliens,bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    # 更新子弹位置
    bullets.update()
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets)

def check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets):
    # 检查是否有子弹击中了外星人
    # 如果是这样，就删除相应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    if len(aliens) == 0:
        # 删除现有的子弹并新建一群外星人
        bullets.empty()
        creat_fleet(ai_settings,screen,ship,aliens)

def creat_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    # 创建一个外星人，并计算一行可容纳多少个外星人
    # 外星人间距为外星人宽度

    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,
                                  alien.rect.height)

    # 创建第一行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # 创建一个外星人并将其加入当前行
            creat_alien(ai_settings,screen,aliens,alien_number,
                        row_number)


def get_number_aliens_x(ai_settings, alien_width):
    """计算每行可容纳多少个外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int((available_space_x) / (2 * alien_width))
    return number_aliens_x

def creat_alien(ai_settings,screen,aliens,alien_number,row_number):
    """创建一个外星人并将其放在当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
    aliens.add(alien)

def get_number_rows(ai_settings,ship_height,alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height-(3*alien_height)
                         -ship_height)
    number_rows = int(available_space_y/(2*alien_height))
    return number_rows

def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """将整群外星人下移，并改变它们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_drop_direction *= -1

def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets):
    """检查外星人是否到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞到一样进行处理
            ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
            break

def update_aliens(ai_settings, stats,screen,ship, aliens,bullets):
    """检查是否有外星人位于屏幕边缘，更新外星人群中所有外星人的位置"""
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets)

    # 检查是否有外星人到达屏幕底端
    check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets)
```

## game_stats.py

```python
class GameStats():
    """跟踪游戏的统计信息"""
    def __init__(self,ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # 游戏刚启动时处于活动状态
        self.game_active = True

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
```

## settings.py

```python
class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230,230,230)

        # 飞船的设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # 子弹设置,宽3像素，高15像素的深灰色子弹
        self.bullet_speed_factor = 3
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3

        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction为表示向右移，为-1表示向左移动
        self.fleet_drop_direction = 1
```

## ship.py

```python
import pygame

class Ship():
    def __init__(self,ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            self.center -= self.ai_settings.ship_speed_factor

        # 根据self.center更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx
```

## 第十三章小结

- 创建一群外星人
- update()方法移动大量元素
- 控制对象在屏幕上移动的方向
- 跟踪统计信息

# 第十四章：计分

## alien.py

```python
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人的类"""
    def __init__(self,ai_settings,screen):
        """初始化外星人并设置其起始位置"""
        super(Alien,self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        # 加载外星人图像，并设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image,self.rect)

    def check_edges(self):
        """如果外星人位于屏幕边缘，就返回True"""
        self_rect = self.screen.get_rect()
        if self.rect.right >= self.screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """向右移动外星人"""
        self.x += (self.ai_settings.alien_speed_factor *
                    self.ai_settings.fleet_direction)
        self.rect.x = self.x
```

## alien_invasion.py

```python
import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from Scoreboard import Scoreboard
from ship import Ship
from alien import Alien
from button import Button
import game_function as gf

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    
    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮
    play_button = Button(ai_settings,screen,"Play")

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)

    # 创建一艘飞船
    ship = Ship(ai_settings,screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 创建外星人群
    aliens = Group()
    gf.creat_fleet(ai_settings,screen,ship,aliens)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,
                         play_button)

if __name__ == '__main__':
    run_game()
```

## bullet.py

```python
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类"""

    def __init__(self,ai_settings,screen,ship):
        """在飞船所处的位置创建一个子弹对象"""
        super(Bullet, self).__init__()
        self.screen = screen

        # 在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储用小数表示的子弹的位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动的子弹"""
        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor
        # 更新表示子弹的rect位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)
```

## button.py

```python
import pygame.font

class Button():
    def __init__(self,ai_settings,screen,msg):
        """初始化按钮属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 设置按钮的尺寸和其他属性
        self.width, self.height = 200,50
        self.button_color = (0,255,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)

        # 创建按钮的rect对象，并使其居其中
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        # 按钮的标签只创建一次
        self.prep_msg(msg)

    def prep_msg(self,msg):
        """将msg渲染为图像，并使其在按钮上居中"""
        self.msg_image = self.font.render(msg,True,self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # 绘制一个用颜色填充的按钮，再绘制文本
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
```

## game_function.py

```python
import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def ship_hit(ai_setting,screen,stats,sb,ship,aliens,bullets):
    """响应被外星人撞到的飞船"""
    if stats.ships_left > 0:
        # 将ship_left减1
        stats.ships_left -= 1

        # 更新记分牌
        sb.prep_ships()

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并将飞船放到屏幕底端中央
        creat_fleet(ai_setting,screen,ship,aliens)
        ship.center_ship()

        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 向左移动飞船
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):
    # 创建一颗子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings,screen,stats, sb,play_button, ship, aliens,bullets):
    """响应按键和鼠标事件"""
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,sb,play_button,
                              ship,aliens,bullets,mouse_x,mouse_y)

def check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,
                      bullets,mouse_x,mouse_y):
    """在玩家单击Play按钮时开始新游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        # 重置游戏设置
        ai_settings.initialize_dynamic_settings()
        # 隐藏光标
        pygame.mouse.set_visible(False)
        # 重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True
        # 重置记分牌图像
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        # 创建一群外星人，并让飞船居中
        creat_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()

def update_screen(ai_settings, screen, stats,sb,ship,aliens,bullets,play_button):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # 显示得分
    sb.show_score()

    # 如果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    # 更新子弹位置
    bullets.update()
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets)

def check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets):
    # 检查是否有子弹击中了外星人
    # 如果是这样，就删除相应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points*len(aliens)
            sb.prep_score()
        check_high_score(stats,sb)

    if len(aliens) == 0:
        # 删除现有的子弹并新建一群外星人
        # 如果整群外星人被消灭，就提高一个等级
        bullets.empty()
        ai_settings.increase_speed()

        # 提高等级
        stats.level += 1
        sb.prep_level()

        creat_fleet(ai_settings,screen,ship,aliens)

def creat_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    # 创建一个外星人，并计算一行可容纳多少个外星人
    # 外星人间距为外星人宽度

    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,
                                  alien.rect.height)

    # 创建第一行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # 创建一个外星人并将其加入当前行
            creat_alien(ai_settings,screen,aliens,alien_number,
                        row_number)


def get_number_aliens_x(ai_settings, alien_width):
    """计算每行可容纳多少个外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int((available_space_x) / (2 * alien_width))
    return number_aliens_x

def creat_alien(ai_settings,screen,aliens,alien_number,row_number):
    """创建一个外星人并将其放在当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
    aliens.add(alien)

def get_number_rows(ai_settings,ship_height,alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height-(3*alien_height)
                         -ship_height)
    number_rows = int(available_space_y/(2*alien_height))
    return number_rows

def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """将整群外星人下移，并改变它们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def check_aliens_bottom(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """检查外星人是否到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞到一样进行处理
            ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)
            break

def update_aliens(ai_settings, screen,stats,sb,ship, aliens,bullets):
    """检查是否有外星人位于屏幕边缘，更新外星人群中所有外星人的位置"""
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)

    # 检查是否有外星人到达屏幕底端
    check_aliens_bottom(ai_settings,screen,stats,sb,ship,aliens,bullets)

def check_high_score(stats,sb):
    """检查是否诞生了最高分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
```

## game_stats.py

```python
class GameStats():
    """跟踪游戏的统计信息"""
    def __init__(self,ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # 游戏刚启动时处于非活动状态
        self.game_active = False
        # 在任何情况下都不应重置最高得分
        self.high_score = 0

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

```

## Scoreboard.py

```python
import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    """显示得分信息的类"""
    def __init__(self,ai_settings,screen,stats):
        """初始化显示得分涉及的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # 显示得分信息时使用的字体设置
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)

        # 准备初始得分图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """将得分转换为一幅渲染的图像"""
        rounded_score = int(round(self.stats.score,-1))
        score_str = "{:,}".format(rounded_score)
        score_str = "current score: " + score_str

        self.score_image = self.font.render(score_str,True,self.text_color,
                                            self.ai_settings.bg_color)

        # 将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """将最高分转换为渲染的图像"""
        high_score = int(round(self.stats.high_score,-1))
        high_score_str = "{:,}".format(high_score)
        high_score_str = "highest score: "+high_score_str
        self.high_score_image = self.font.render(high_score_str,True,
                                                 self.text_color,self.ai_settings.bg_color)

        # 将最高分放到屏幕顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """将等级转换为渲染的图像"""
        levestr = "level: "+str(self.stats.level)
        self.level_image = self.font.render(levestr,True,
                                            self.text_color,self.ai_settings.bg_color)
        # 将等级放在得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        # 绘制飞船
        self.ships.draw(self.screen)

    def prep_ships(self):
        """显示还剩余多少飞船"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings,self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
```

## settings.py

```python
class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230,230,230)

        # 飞船的设置
        # self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # 子弹设置,宽3像素，高15像素的深灰色子弹
        self.bullet_speed_factor = 3
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3

        # 外星人设置
        # self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction为表示向右移，为-1表示向左移动
        #self.fleet_drop_direction = 1

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        # 外星人点数的提高速度
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction为1表示向右，为-1表示向左
        self.fleet_direction = 1

        # 计分
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points*self.score_scale)
        print(self.alien_points)
```

## ship.py

```python
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self,ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        super(Ship,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            self.center -= self.ai_settings.ship_speed_factor

        # 根据self.center更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx
```

## 第十四章小结

- play按钮
- 检测鼠标事件
- 隐藏光标

# 第十五章：生成数据

## 绘制简单的折线图

```python
import matplotlib.pyplot as plt

if __name__ == '__main__':

    input_value = [1,2,3,4,5]
    squares = [1,4,9,16,25]
    plt.plot(input_value,squares,linewidth=5)
    # 设置标题，并给坐标轴加上标签
    plt.title("Square Numbers",fontsize=24)
    plt.xlabel("value",fontsize=14)
    plt.ylabel("Square of value",fontsize=14)
    # 设置刻度标记的大小
    plt.tick_params(axis='both',labelsize=14)

    plt.show()
```

## 绘制散点

```python
plt.scatter(2,4,s=200)
# 设置图标标题并给坐标轴加上标签
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of value",fontsize=14)
# 设置刻度标记的大小
plt.tick_params(axis='both',which='major',labelsize=14)
plt.show()
```

## 绘制一系列散点

```python
    x_values = [1,2,3,4,5]
    y_values = [1,4,9,16,25]

    plt.scatter(x_values,y_values,s=100)
    # 设置图标标题并给坐标轴加上标签
    plt.title("Square Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of value", fontsize=14)
    # 设置刻度标记的大小
    plt.tick_params(axis='both', which='major', labelsize=14)
    plt.show()
```

```python
    x_values = list(range(1,1001))
    y_values = [x**2 for x in x_values]

    plt.scatter(x_values,y_values,c='red',edgecolors='none',s=40)
    # 设置图标标题并给坐标轴加上标签
    plt.title("Square Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of value", fontsize=14)
    # 设置刻度标记的大小
    plt.tick_params(axis='both', which='major', labelsize=14)
    # 设置每个坐标轴的取值范围
    plt.axis([0,1100,0,1100000])

    plt.show()
```

### 使用颜色映射

```python
    x_values = list(range(1,1001))
    y_values = [x**2 for x in x_values]
    # 根据每个点的y值来设置颜色
    plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,
                edgecolors='none',s=40)
    # 设置图标标题并给坐标轴加上标签
    plt.title("Square Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of value", fontsize=14)
    # 设置刻度标记的大小
    plt.tick_params(axis='both', which='major', labelsize=14)
    # 设置每个坐标轴的取值范围
    plt.axis([0,1100,0,1100000])

    plt.show()
```

### 自动保存图表

```python
    x_values = list(range(1,1001))
    y_values = [x**2 for x in x_values]
    # 根据每个点的y值来设置颜色
    plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,
                edgecolors='none',s=40)
    # 设置图标标题并给坐标轴加上标签
    plt.title("Square Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of value", fontsize=14)
    # 设置刻度标记的大小
    plt.tick_params(axis='both', which='major', labelsize=14)
    # 设置每个坐标轴的取值范围
    plt.axis([0,1100,0,1100000])

    plt.savefig('square_plot.png',bbox_inches='tight')
```

## 随机漫步

### random_walk.py

```python
from random import choice

class RandomWalk():
    """一个生成随机漫步数据的类"""

    def __init__(self,num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points
        # 所有随机漫步都始于（0,0）
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有点"""
        # 不断漫步，直到列表达到指定的长度
        while len(self.x_values) < self.num_points:
            # 决定前进方向及这个方向的距离
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction*x_distance

            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction*y_distance

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x值和y值
            next_x = self.x_values[-1]+x_step
            next_y = self.y_values[-1]+y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
```

### main.py

```python
import matplotlib.pyplot as plt
from random_walk import RandomWalk

if __name__ == '__main__':
    while True:
        # 创建一个RandomWalk实例，并将其包含的点都绘制出来
        rw = RandomWalk()
        rw.fill_walk()

        plt.scatter(rw.x_values,rw.y_values,s=15)
        plt.show()

        keep_running = input("再走一次？(y/n): ")
        if keep_running.lower() == 'n':
            break
```

## 图表可视化-掷1个骰子

### die.py

```python
from random import randint

class Die():
    """表示一个骰子的类"""

    def __init__(self,num_sides=6):
        """骰子默认为6面"""
        self.num_sides = num_sides

    def roll(self):
        """返回一个位于1和骰子面之间的随机值"""
        return randint(1,self.num_sides)
```

### die_visual.py

```python
from die import Die
import pygal

# 创建一个D6
die = Die()

# 掷骰子几次，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)


# 分析结果
frequencies = []
for value in range(1,die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg') # svg文件可用浏览器打开
```

## 图表可视化-掷2个骰子

### die.py

```python
from random import randint

class Die():
    """表示一个骰子的类"""

    def __init__(self,num_sides=6):
        """骰子默认为6面"""
        self.num_sides = num_sides

    def roll(self):
        """返回一个位于1和骰子面之间的随机值"""
        return randint(1,self.num_sides)
```

### die_visual.py

```python
from die import Die
import pygal

# 创建一个D6
die_1 = Die()
die_2 = Die()

# 掷骰子几次，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die_1.roll()+die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = list(range(2,13))
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6+D6',frequencies)
hist.render_to_file('die_visual.svg')
```

## 第十五章小结

- 生成数据集
- 折线图、散点图、直方图
- 颜色映射、自动保存图表

# 第十六章：下载数据

## 读取csv数据的表头

```python
import csv

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index,colum_header in enumerate(header_row):
        print(index,colum_header)
```

## 绘制气温图表

```python
import csv
from matplotlib import pyplot as plt
from datetime import datetime

# 从文件中获取最高气温
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0],"%Y-%m-%d")
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)

    print(highs)

# 根据数据绘制图形
fig = plt.figure(dpi=128,figsize=(8,4))
plt.plot(dates,highs,c='red')

# 设置图形的格式
plt.title("Daily high temperatures, July 2004",fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()
```

## 给图表区域着色

```python
import csv
from matplotlib import pyplot as plt
from datetime import datetime

# 从文件中获取最高气温
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0],"%Y-%m-%d")
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)

        low = int(row[3])
        lows.append(low)

# 根据数据绘制图形
fig = plt.figure(dpi=128,figsize=(8,4))
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

# 设置图形的格式
plt.title("Daily high temperatures-2004",fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()
```

## 异常处理

```python
import csv
from matplotlib import pyplot as plt
from datetime import datetime

# 从文件中获取最高气温
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0],"%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date,'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# 根据数据绘制图形
fig = plt.figure(dpi=128,figsize=(8,4))
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

# 设置图形的格式
plt.title("Daily high and low temperatures-2004\nDeath Valley, CA",fontsize=14)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()
```
