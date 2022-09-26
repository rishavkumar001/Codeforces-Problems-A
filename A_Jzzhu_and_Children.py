import math
n,k=map(int,input().split())
l=list(map(int,input().split()[:n]))
ans=-1
p=-1
for i in range(n):
    temp=math.ceil(l[i]/k)
    if temp>=ans:
        ans=temp
        p=i+1
print(p)