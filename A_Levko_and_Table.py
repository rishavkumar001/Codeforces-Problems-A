n,k=map(int,input().split())
l=[]
for i in range(n):
    l.append([0]*n)
for i in range(n):
    l[i][i]=k
for i in l:
    for j in i:
        print(j,end=" ")
    print()