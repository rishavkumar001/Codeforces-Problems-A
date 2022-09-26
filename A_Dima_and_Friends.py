n=int(input())
l=list(map(int,input().split()))
s=sum(l)
cc=0
for i in range(1,6):
    if (s+i)%(n+1)!=1:
        cc+=1
print(cc)