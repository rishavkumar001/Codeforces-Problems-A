for _ in range(int(input())):
    n=int(input())
    s=input()
    c,ans=0,0
    for i in s:
        if i==")":
            c+=1
        else:
            c-=1
        ans=max(ans,c)
    print(ans)