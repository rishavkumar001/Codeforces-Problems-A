m,n=map(int,input().split())
a=0
c=0
while a*a<=m and a<=n:
    b=m-a*a
    if a+(b*b)==n:
        c+=1
    a+=1
print(c)