for _ in range(int(input())):
    n,a,b=map(int,input().split())
    s='a'
    res='a'
    for i in range(b-1):
        res=res+chr(ord(s)+1+i)
    for i in range(a-b):
        res=res+res[-1]
    for i in range(n-a):
        res=res+res[i%a]
    print(res)