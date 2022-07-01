n=int(input())
arr=list(map(int,input().split()))
a=b=0
for i in arr:
    if i%2!=0:
        b+=1
    else:
        a+=1
print(a,b)