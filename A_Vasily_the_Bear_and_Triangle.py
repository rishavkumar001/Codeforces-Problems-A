x,y=map(int,input().split())
x1,x2,y1,y2=0,0,0,0
if x<0:
    x1=x-abs(y)
else:
    x1=x+abs(y)
if y<0:
    y2=y-abs(x)
else:
    y2=y+abs(x)
if x1>x2:
    x1,x2=x2,x1
    y1,y2=y2,y1
print(x1,end=" ")
print(y1,end=" ")
print(x2,end=" ")
print(y2,)