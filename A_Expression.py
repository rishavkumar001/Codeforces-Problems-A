a=int(input())
b=int(input())
c=int(input())
if a==1 and c==1:
    print(b+1+1)
elif a==1:
    print((a+b)*c)
elif c==1:
    print(a*(b+c))
else:
    print(max(a*b*c,(min(a,c)+b)*max(a,c)))