l=[]
for i in range(3):
    l.append(list(map(int,input().split())))
t=[]
t.append([0,0,0,0,0])
for i in range(3):
    li=[]
    li.append(0)
    for j in range(3):
        li.append(l[i][j])
    li.append(0)
    t.append(li)
t.append([0,0,0,0,0])
for i in range(1,4):
    for j in range(1,4):
        if (t[i][j]+t[i+1][j]+t[i-1][j]+t[i][j+1]+t[i][j-1])%2:
            l[i-1][j-1]=0
        else:
            l[i-1][j-1]=1
for i in l:
    for j in i:
        print(j,end="")
    print()