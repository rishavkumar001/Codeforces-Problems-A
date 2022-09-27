n=int(input())
l=list(map(int,input().split()))
p1,p2=0,n-1
i=0
s1,s2=0,0
while not p1>p2:
    if i%2==0:
        s1+=max(l[p1],l[p2])
    else:
        s2+=max(l[p1],l[p2])
    if l[p1]>l[p2]:
        p1+=1
    else:
        p2-=1
    i+=1
print(s1,end=" ")
print(s2)