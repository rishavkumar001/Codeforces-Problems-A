n,k=map(int,input().split())
l=[]
for _ in range(n):
    l.append(list(map(int,input().split())))
ans=-9999999999
for i in l:
    if i[1]>k:
        ans=max(ans,i[0]-i[1]+k)
    else:
        ans=max(ans,i[0])
print(ans)