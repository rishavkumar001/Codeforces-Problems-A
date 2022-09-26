for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    m=max(l)
    for i in range(len(l)):
        if l[i]==m:
            print(i+1)
            break