n=int(input())
if n==0:
    print(1)
else:
    n=n%4
    if n==0:
        print(6)
    elif n==1:
        print(8)
    elif n==2:
        print(4)
    elif n==3:
        print(2)