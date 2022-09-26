n=int(input())
s1,s2=0,0
for _ in range(n):
    a,b=map(int,input().split())
    s1+=a
    s2+=b
print(min(s1,n-s1)+min(s2,n-s2))