m=int(input())
n=int(input())
while n:
    a,b=map(int,input().split())
    if a<m or b<m:
        print("UPLOAD ANOTHER")
    elif a==b:
        print("ACCEPTED")
    else:
        print("CROP IT")
    n-=1