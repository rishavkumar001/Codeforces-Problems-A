n,k=map(int,input().split())
l=list(map(int,input().split()))
ans=[]
for i in range(k):
    ans.append([l[i]])
ptr=0
for i in range(1,n*k+1):
    if len(ans[ptr])==n:
        ptr+=1
    if ptr==k:
        break
    if i not in l:
        ans[ptr].append(i)
for i in ans:
    for j in i:
        print(j,end=" ")
    print()