n,m=map(int,input().split())
if m>n:
    print(-1)
else:
    a=n//2
    b=n%2
    while a!=0 and (a+b)%m!=0:
            a-=1
            b+=2
    print(a+b)