d={}
for _ in range(int(input())):
    s=input()
    if s not in d:
        d[s]=1
    else:
        d[s]+=1
m=d[s]
ans=s
for i in d:
    if d[i]>m:
        m=d[i]
        ans=i
print(ans)