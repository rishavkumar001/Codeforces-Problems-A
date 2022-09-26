n=int(input())
l=list(map(int,input().split()))
m=min(l)
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
if d[m]!=1:
    print("Still Rozdil")
else:
    for i in range(n):
        if l[i]==m:
            print(i+1)
            break