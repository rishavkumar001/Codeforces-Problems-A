n=int(input())
for i in range(n+1,1000000):
    t=i
    d={}
    flag=1
    while t!=0:
        if t%10 not in d:
            d[t%10]=1
        else:

            flag=0
            break
        t=t//10
    if flag==1:
        print(i)
        break