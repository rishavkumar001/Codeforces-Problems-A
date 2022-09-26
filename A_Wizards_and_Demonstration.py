import math
n,x,y=map(int,input().split())
if math.ceil(n*y/100)-x<0:
    print(0)
else:
    print(math.ceil(n*y/100)-x)