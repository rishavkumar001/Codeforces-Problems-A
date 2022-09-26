n1=int(input())
l1=list(map(int,input().split()))
n2=int(input())
l2=list(map(int,input().split()))
d={}
ma=0
count=0
for i in l1:
    for j in l2:
        if j%i==0:
            if j//i>ma:
                count=1
                ma=j//i
            elif j//i==ma:
                count+=1
print(count)