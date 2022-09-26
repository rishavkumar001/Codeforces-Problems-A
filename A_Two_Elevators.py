for _ in range(int(input())):
    a,b,c=map(int,input().split())
    t=abs(b-c)+c
    if t>a:
        print(1)
    elif t==a:
        print(3)
    else:
        print(2)