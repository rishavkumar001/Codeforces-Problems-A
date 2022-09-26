n=int(input())
l=list(map(int,input().split()))
l.sort()
ptr=11
s=0
c=0
while s<n and ptr!=-1:
    s+=l[ptr]
    ptr-=1
    c+=1
if s<n:
    print(-1)
else:
    print(c)