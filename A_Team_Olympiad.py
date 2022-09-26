n=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(3):
    a.append([])
for i in range(n):
    a[l[i]-1].append(i+1)
t=min(len(a[0]),len(a[1]),len(a[2]))
if t==0:
    print(0)
else:
    print(t)
    for i in range(t):
        for j in range(3):
            print(a[j][i],end=" ")
        print()