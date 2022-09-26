n=int(input())
l=list(map(int,input().split()))
p=0
l1,l2,l3=[],[],[]
for i in l:
    if i<0:
        l1.append(i)
    elif i==0:
        l3.append(i)
    else:
        l2.append(i)
if len(l2)==0:
    l2.append(l1.pop())
    l2.append(l1.pop())
if len(l1)%2==0:
    l3.append(l1.pop())
print(len(l1),end=" ")
for i in l1:
    print(i,end=" ")
print()
print(len(l2),end=" ")
for i in l2:
    print(i,end=" ")
print()
print(len(l3),end=" ")
for i in l3:
    print(i,end=" ")