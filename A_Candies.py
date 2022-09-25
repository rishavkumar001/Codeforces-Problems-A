for _ in range(int(input())):
    n=int(input())
    m=1
    for i in range(49):
        m=2*m+1
        if n%m==0:
            print(n//m)
            break