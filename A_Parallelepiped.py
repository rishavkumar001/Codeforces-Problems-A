p,q,r=map(int,input().split())
a=(p*q//r)**0.5
b=(q*r//p)**0.5
c=(r*p//q)**0.5
print(4*int(a+b+c))