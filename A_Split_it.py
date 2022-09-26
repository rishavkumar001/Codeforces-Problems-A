for _ in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    p1,p2=0,len(s)-1
    flag=1
    if len(s)<2*k+1:
        print("NO")
    else:
        while p1!=k and p2>p1:
            if s[p1]!=s[p2]:
                flag=0
                break
            p1+=1
            p2-=1
        if flag :
            print("YES")
        else:
            print("NO")