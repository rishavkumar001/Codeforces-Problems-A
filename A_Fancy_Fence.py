for _ in range(int(input())):
    n=int(input())
    if 360/(180-n)==360//(180-n):
        print("YES")
    else:
        print("NO")