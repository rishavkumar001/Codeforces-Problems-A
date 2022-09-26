n=int(input())
l=list(map(int,input().split()))
t=l[0]
i=0
while t<n:
    i=i+1
    i=i%7
    t=t+l[i]
print(i+1)