x,y,a,b=map(int,input().split())
l=[]
while a<=b and x>a:
    a+=1
while a<=x:
    t=b
    while t<a and t<=y: 
        l.append([a,t])
        t+=1
    a+=1
print(len(l))
for i in l:
    print(i[0],end=" ")
    print(i[1])