n=input()
if int(n)>=0:
    print(int(n))
else:
    if len(n)==2:
        print(0)
    elif int(n[-1])>=int(n[-2]):
        n=n[:-1]
        print(int(n))
    else:
        n=n[:-2]+n[-1:]
        print(int(n))