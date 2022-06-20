k=int(input())
f=0
s=1
n=f+s
print(f,s,n,end=" ")
while k-3:
    f=s
    s=n
    n=f+s
    print(n,end=" ")
    k-=1