for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    x=0
    a.sort()
    for i in range(0,n-2,3):
        ans=max(a[i+2]-a[i],x)
    print(ans)