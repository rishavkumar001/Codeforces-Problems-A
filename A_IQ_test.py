n=int(input())
l=list(map(int,input().split()))
d={}
for i in range(1,n):
    x=l[i]-l[i-1]
    if x not in d:
        d[x]=1
    else:
        d[x]+=1
print(d)
diff=0
p=99999999
for i in d:
    if d[i]<p:
        diff=i
print(diff)