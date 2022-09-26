x1,y1,x2,y2=map(int,input().split())
if (x1!=x2 and y1!=y2) and abs(x1-x2)!=abs(y1-y2):
    print(-1)
elif x1==x2:
    x3=x1+abs(y1-y2)
    x4=x1+abs(y1-y2)
    y3,y4=y1,y2
    print(x3, y3, x4, y4)
elif y1==y2:
    y3=y1+abs(x1-x2)
    y4=y1+abs(x1-x2)
    x3,x4=x1,x2
    print(x3, y3, x4, y4)
else:
    x3=x1
    y3=y2
    x4=x2
    y4=y1
    print(x3, y3, x4, y4)