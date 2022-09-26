for _ in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    p=0
    for i in range(n):
        nu=l[i]
        ind=i
        if p<k:
            for j in range(i,n,k):

                if l[j]>nu:
                    ind=j
                    nu=l[j]
            if nu!=l[i]:
                p+=1
                l[i],l[ind]=l[ind],l[i]
    print(sum(l[:k]))