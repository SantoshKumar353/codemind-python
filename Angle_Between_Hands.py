m,n=list(map(int,input().split(':')))
v=abs(30*m-((11/2)*n))
k=360-v
if v<k:
    print(v)
else:
    print(k)