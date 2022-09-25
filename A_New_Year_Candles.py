a,b=map(int,input().split())
ans=a
while a>=b:
    x=a%b
    a=a//b
    ans+=a
    a=a+x
print(ans)