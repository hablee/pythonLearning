本题要求编写程序，输出菲波那契（Fibonacci）数列的前N项，每行输出5个，题目保证输出结果在长整型范围内。
Fibonacci数列就是满足任一项数字是前两项的和（最开始两项均定义为1）的数列，例如：1，1，2，3，5，8，13，...。
# 输入格式:
输入在一行中给出一个整数N（1≤N≤46）。
# 输出格式:
输出前N个Fibonacci数，每个数占11位，每行输出5个。如果最后一行输出的个数不到5个，也需要换行。如果N小于1，则输出"Invalid."
# 输入样例1:
`7`
# 输出样例1:
```python
      1          1          2          3          5
      8         13
```
# 输入样例2：
`0`
# 输出样例2：
`Invalid.`
# 解答
```python
N = int(input())
cnt = 0
if N==0:
        print('Invalid.')
elif N==1:
        
        fibFi = 1
        print('{:11d}'.format(fibFi),end='')
        cnt = cnt + 1
elif N==2:
        fibFi = 1
        print('{:11d}'.format(fibFi),end='')
        cnt = cnt + 1
        fibSc = 1
        print('{:11d}'.format(fibSc),end='')
        cnt = cnt + 1
else:
        fib=[]
        fibFi = 1
        fibSc = 1
        print('{:11d}'.format(fibFi),end='')
        cnt = cnt + 1
        print('{:11d}'.format(fibSc),end='')
        cnt = cnt + 1
        fib.append(fibFi)
        fib.append(fibSc)
        for i in range(N-2):
                fibTh= fibFi + fibSc
                print('{:11d}'.format(fibTh),end='')
                cnt = cnt + 1
                if cnt%5==0:
                        print()
                fib.append(fibTh)
                fibFi = fibSc
                fibSc = fibTh
        if cnt%5!=0:
                print()
```
# 测试结果
答案正确
# 思路
主要还是要注意空格和换行的条件，不要用递归算fib，时间开销大
