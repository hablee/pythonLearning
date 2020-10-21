在练习 6-4 中，你使用了一个标准字典来表示词汇表。请
使用 OrderedDict 类来重写这个程序，并确认输出的顺序与你在字典中添加键—值对的
顺序一致。
# 代码
```python
from collections import OrderedDict

wordList = OrderedDict()

wordList['good'] = '好'
wordList['moring'] = '早上'
wordList['ten'] = '十'

for English, Chinese in wordList.items():
    print(English+": "+Chinese)
```
# 输出
```python
good: 好
moring: 早上
ten: 十
```
