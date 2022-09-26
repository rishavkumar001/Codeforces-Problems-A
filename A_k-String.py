n=int(input())
s=input()
d={}
flag=0
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
ans=""
for i in d:
    if d[i]%n!=0:
        flag=1
        break
    else:
        for x in range(d[i]//n):
            ans+=i
if flag==1:
    print(-1)
else:
    res=""
    for i in range(n):
        res=res+ans
    print(res)