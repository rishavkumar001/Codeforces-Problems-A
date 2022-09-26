a=0
for i in range(8):
    s=input()
    for j in range(7):
        if s[j]==s[j+1]:
            a=1
if a==0:
    print("YES")
else:
    print("NO")