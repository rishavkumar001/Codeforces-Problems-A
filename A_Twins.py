n=int(input())
l=list(map(int,input().split()))
l.sort()
s1,t=0,sum(l)
c=0
while t-s1>=s1:
    s1=s1+l[-1-c]
    c+=1
print(c)