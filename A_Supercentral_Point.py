n=int(input())
l=[]
for i in range(n):
    t=list(map(int,input().split()))
    l.append(t)
c=0
for i in range(len(l)):
    a=l[i][0]
    b=l[i][1]
    p=[0,0,0,0]
    for j in range(n):
        if l[j][0]>a and l[j][1]==b:
            p[0]=1
        elif l[j][0]<a and l[j][1]==b:
            p[1]=1
        elif l[j][0]==a and l[j][1]>b:
            p[2]=1
        elif l[j][0]==a and l[j][1]<b:
            p[3]=1
    if sum(p)==4:
        c+=1
print(c)