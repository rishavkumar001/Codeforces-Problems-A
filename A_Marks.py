n,x=map(int,input().split())
se=set()
l=[]
for i in range(x):
    l.append([])
for i in range(n):
    s=input()
    for a in range(len(s)):
        l[a].append(int(s[a]))
for i in range(len(l)):
    m=max(l[i])
    for j in range(len(l[i])):
        if l[i][j]==m:
            se.add(j)
print(len(se))