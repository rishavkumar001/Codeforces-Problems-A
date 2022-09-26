for _ in range(int(input())):
    n,x=list(map(int,input().split()))
    l=list(map(int,input().split()))
    l.sort()
    flag=1
    for i in range(n):
        if l[n+i]-l[i]<x:
            flag=0
            break
    if flag==0:
        print("NO")
    else:
        print("YES")