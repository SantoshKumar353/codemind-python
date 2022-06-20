k=int(input())
arr=list(map(int,input().split()))
min=arr[0]
count=0
for i in range(0,k):
    if min>arr[i]:
        min=arr[i]
while min:
    count=0
    for j in range(0,k):
        if arr[j]%min==0:
            count+=1
    if count==k:
        print(min)
        break
    min-=1