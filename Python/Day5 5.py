"""
生成斐波那契数列的前20个数
"""
num = int(input('How many do you want:'))
n1 = 1
n2 = 0
count = 0
while count < num:
    Fibonacci = n1 + n2
    n2 = n1
    n1 = Fibonacci
    count += 1
    print(Fibonacci,end=' ')
print()