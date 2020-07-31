a = float(input('a ='))
b = float(input('b ='))
c = float(input('c ='))

if  a+b>c and a+c>b and b+c >a:
    print('zhouchang is %f' %(a+b+c))
    p = (a+b+c)/2
    area = (p*(p-a)*(p-b)*(p-c))**0.5
    print('Area is %f'%area)
else:
    print('not triangle')