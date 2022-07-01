def min_dig(k):
    a=list(map(int,input().split()))
    m=min(a)
    c=0
    for i in a:
        if len(str(m))==len(str(i)):
            c+=1
    print(c)
    
k=int(input())
min_dig(k)