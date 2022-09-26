n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if i==5:
        c+=1
val=0
for i in range(c):
    val=val*10+5
t=(10**(n-c))
if n-c!=0:
    x=val
    while x%9!=0:
        x=x//10
    if x!=0:
        print(x*t)
    else:
        print(0)
else:
    print(-1)