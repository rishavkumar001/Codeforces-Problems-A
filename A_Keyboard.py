n=input()
st=input()
s="qwertyuiopasdfghjkl;zxcvbnm,./"
if n=="R":
    c=-1
else:
    c=1
ans=""
for i in range(len(st)):
    for j in range(len(s)):
        if st[i]==s[j]:
            ans+=s[j+c]
print(ans)