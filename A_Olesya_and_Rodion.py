n,t=map(int,input().split())
a=str(t)
if len(a)>n:
    print(-1)
else:
    print(t,end="")
    for i in range(n-len(a)):
        print(0,end="")
