for _ in range(int(input())):
    n=int(input())
    a=str(bin(n))
    c=0
    if a[2]=='1':
        for i in a[3:]:
            c+=int(i)
    if c==0:
        print("NO")
    else:
        print("YES")