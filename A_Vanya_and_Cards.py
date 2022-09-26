n,x=map(int,input().split())
l=list(map(int,input().split()))
s=abs(sum(l))
c=0
if s==0:
    print(0)
elif s<=x:
    print(1)
else:
    if s%x:
        print(1+s//x)
    else:
        print(s//x)