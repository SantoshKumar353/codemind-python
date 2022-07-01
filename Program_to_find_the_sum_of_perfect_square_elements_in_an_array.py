def sum(k):
    s=int(k**0.5)
    if s*s==k:
        return True
    else:
        return False
k=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    if sum(i):
        s+=i
print(s)