s=input()
flag=0
for i in range(len(s)):
    if s[i] in "HQ9":
        flag=1
        break
if flag==1:
    print("YES")
else:
    print("NO")