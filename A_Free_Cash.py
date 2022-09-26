x=0
l=[]
d={}
for _ in range(int(input())):
    a,b=list(map(int,input().split()))
    if a not in d:
        d[a]=x
        x+=1
        l.append([b])
    else:
        l[d[a]].append(b)
ans=1
for i in l:
    x=sorted(i)
    d1={}
    for j in x:
        if j not in d1:
            d1[j]=1
        else:
            d1[j]+=1
        ans=max(ans,d1[j])
print(ans)