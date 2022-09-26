a=int(input())
b=int(input())
c=a+b
a1,b1,c1=str(a),str(b),str(c)
a2,b2,c2="","",""
for i in a1:
    if i!='0':
        a2+=i
for i in b1:
    if i!='0':
        b2+=i
for i in c1:
    if i!='0':
        c2+=i
if int(a2)+int(b2)==int(c2):
    print("YES")
else:
    print("NO")