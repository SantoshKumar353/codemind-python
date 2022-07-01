k=int(input())
a=list(map(int,input().split()))
for i in range(k-1,(k//2)-1,-1):
    print(a[i],end=' ')
print(*a[0:k//2:1],end=' ')