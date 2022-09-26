n=int(input())
l=[]
for i in range(n):
    l.append([0]*n)
for i in range(n):
    

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
print(l1)
print(l2)
print(l3)
if len(l2)==0:
    l2.append(l1.pop())
    l2.append(l1.pop())
if len(l1)%2:
    l3.append(l1.pop())