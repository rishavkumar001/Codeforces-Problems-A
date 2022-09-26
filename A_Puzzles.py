s,n=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
ans=99999999
for i in range(n-s+1):
    ans=min(ans,l[i+s-1]-l[i])
print(ans)