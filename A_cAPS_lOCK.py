s=input()
a1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
a2="abcdefghijklmnopqrstuvwxyz"
c1=0
c2=0
for i in s:
    if i in a1:
        c1+=1
    elif i in a2:
        c2+=1
if c1==len(s)-1 and s[0] in a2:
    print(chr(ord(s[0])-32),end="")
    for i in s[1:]:
        print(chr(ord(i)+32),end="")
    print()
elif c1==len(s):
    for i in s:
        print(chr(ord(i)+32),end="")
    print()
else:
    print(s)