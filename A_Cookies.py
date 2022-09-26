n=int(input())
l=list(map(int,input().split()))
c,o=0,0
for i in l:
    if i%2==0:
        c+=1
    else:
        o+=1
if sum(l)%2:
    print(o)
else:
    print(c)