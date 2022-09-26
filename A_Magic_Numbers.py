s=input()
flag=0
t=0
for i in range(len(s)-1,-1,-1):
    if s[i]=='1':
        t=0
    elif s[i]=='4':
        if t==2:
            flag=1
            break
        t+=1
    else:
        flag=1
        break
if flag==1 or t!=0:
    print("NO")
else:
    print("YES")