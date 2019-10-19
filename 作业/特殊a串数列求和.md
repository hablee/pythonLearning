给定两个均不超过9的正整数a和n，要求编写程序求a+aa+aaa++⋯+aa⋯a（n个a）之和。
# 输入格式：
输入在一行中给出不超过9的正整数a和n。
# 输出格式：
在一行中按照“s = 对应的和”的格式输出。
# 输入样例：
`2 3`
# 输出样例：
`s = 246`

# 解答
```python
a,n = input().split()
sum_re = 0;
for i in range(1,int(n)+1):
    sum_re = sum_re + (int(a*i))
print('s =',sum_re)
```
