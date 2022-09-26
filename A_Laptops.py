l=[]
for _ in range(int(input())):
    l.append(list(map(int,input().split())))
l.sort()
flag=0
for i in range(len(l)-1):
    if l[i][1]>l[i+1][1]:
        flag=1
        break
if flag:
    print("Happy Alex")
else:
    print("Poor Alex")