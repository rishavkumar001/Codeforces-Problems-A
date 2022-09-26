n=int(input())
l=list(map(int,input().split()))
l.sort()
flag=1
for i in range(n):
    if l[i]-1!=i:
        print(i+1)
        flag=0
        break
if flag:
    print(n+1)