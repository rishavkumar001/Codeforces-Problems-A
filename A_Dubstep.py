s=input()
ans=""
i=0
if len(s)<3:
    print(s)
else:
    while i<len(s)-2:
        a=s[i]
        b=s[i+1]
        c=s[i+2]
        if a=="W" and b=="U" and c=="B":
            if len(ans)!=0 and ans[-1]!=" ":
                ans+=" "
            i+=3
        else:
            ans+=a
            i+=1
    if len(s)>3 and (s[-4]=='W' and s[-3]=="U" and s[-2]=="B"):
        ans+=s[-1]
    elif (s[-3]=='W' and s[-2]=="U" and s[-1]=="B"):
        pass
    else:
        ans+=s[-2]
        ans+=s[-1]
    print(ans)
