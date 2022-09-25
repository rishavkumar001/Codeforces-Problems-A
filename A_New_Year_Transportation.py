n,t=map(int,input().split())
l=list(map(int,input().split()))
a=[0]*n
a[t-1]=1
for i in range(t-2,-1,-1):
    if a[i+l[i]]==1:
        a[i]=1
if a[0]==1:
    print("YES")
else:
    print("NO")