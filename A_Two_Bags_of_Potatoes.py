y,k,n=map(int,input().split())
x=k*(1+y//k)-y
flag=0
while x+y<=n:
    flag=1
    print(x,end=" ")
    x+=k
if flag==0:
    print(-1)