r,c=map(int,input().split())
l=[]
count=0
a,b=0,0
for i in range(r):
    l.append(input())
for i in l:
    flag=0
    for j in i:
        if j=="S":
            flag=1
            break
    if flag==0:
        count+=c
        a+=1
for i in range(c):
    flag=0
    for j in range(r):
        if l[j][i]=="S":
            flag=1
            break
    if flag==0:
        count+=r
        b+=1
    else:
        flag=0
print(count-(a*b))
