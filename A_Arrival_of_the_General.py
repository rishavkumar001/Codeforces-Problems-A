n=int(input())
l=list(map(int,input().split()))
ma=-9999
mi=9999
mai=-1
mii=-1
for i in range(n):
    if l[i]>ma:
        ma=l[i]
        mai=i
for i in range(n-1,-1,-1):
    if l[i]<mi:
        mi=l[i]
        mii=i
if mai<mii:
    print(mai+n-mii-1)
else:
    print(mai+n-mii-2)