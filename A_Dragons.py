s,n=map(int,input().split())
l=[]
flag=0
for _ in range(n):
    a=list(map(int,input().split()))
    l.append(a)
l.sort()
for i in l:
    if i[0]<s:
        s=s+i[1]
    else:
        flag=1
        break
if flag==1:
    print("NO")
else:
    print("YES")