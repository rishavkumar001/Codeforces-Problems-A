a=int(input())
l=int(input())
m=int(input())
n=int(input())
d=int(input())
x={}
for i in range(d):
    x[i+1]=1
k=a
while k<=d:
    x[k]-=1
    k=k+a
k=l
while k<=d:
    x[k]-=1
    k=k+l
k=m
while k<=d:
    x[k]-=1
    k=k+m
k=n
while k<=d:
    x[k]-=1
    k=k+n
c=0
for i in x:
    if x[i]==1:
        c+=1
print(d-c)