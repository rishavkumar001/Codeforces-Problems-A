n=int(input())
l=list(map(int,input().split()))
a=1
m=1
for i in range(1,n):
    if l[i]<l[i-1]:
        a=1
    else:
        a+=1
    m=max(m,a)
print(m)