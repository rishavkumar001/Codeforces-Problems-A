n=int(input())
s=input()
c=0
for i in s:
    if i=="1":
        c+=1
print(len(s)-2*min((len(s)-c),c))