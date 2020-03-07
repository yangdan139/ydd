import math
print('please input three numbers:')
a = int(input())
b = int(input())
c = int(input())
d = int((b*b)-(4*a*c))
if d<0:
    print('这个一元二次方程无解！')

elif d ==0:

    x = (-b)/2*a
    print('该方程有一个唯一解，这个解为：')
    print(x)

else:
    y = (-b+math.sqrt(d))/(2*a)
    z = (-b-math.sqrt(d))/(2*a)
    print ('该方程有两个不同解！')
    print (y)
    print(z)
    


