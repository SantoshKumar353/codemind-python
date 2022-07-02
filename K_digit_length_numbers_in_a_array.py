m,n=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in l:
    if len(str(abs(i)))==n:
        c+=1
print(c)