a,b,c,d=map(int,input().split())
a1=max(3*a/10,a-a*c//250)
a2=max(3*b/10,b-b*d//250)
if a1==a2:
    print("Tie")
elif a1<a2:
    print("Vasya")
else:
    print("Misha")