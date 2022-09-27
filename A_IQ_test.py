n=int(input())
l=list(map(int,input().split()))
l1,l2=[],[]
for i in range(len(l)):
    if l[i]%2:
        l1.append(i+1)
    else:
        l2.append(i+1)
if len(l1)>len(l2):
    print(l2[0])
else:
    print(l1[0])