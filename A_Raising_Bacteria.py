n=int(input())
s=bin(n)[2:]
c=0
for i in s:
    c=c+int(i)
print(c)