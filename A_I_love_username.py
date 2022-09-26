n=int(input())
l=list(map(int,input().split()))
ma=l[0]
mi=l[0]
ans=0
for i in range(1,n):
    if l[i]<mi:
        ans+=1
        mi=l[i]
    elif l[i]>ma:
        ans+=1
        ma=l[i]
print(ans)