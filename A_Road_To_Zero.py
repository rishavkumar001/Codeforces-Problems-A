for _ in range(int(input())):
    m,n=map(int,input().split())
    a,b=map(int,input().split())
    print(min((m+n)*a,min(m,n)*b+abs(m-n)*a,abs(m-n)*a+max(m,n)*b))