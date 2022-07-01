def count(k):
    l=list(map(int,input().split()))
    N=[]
    for i in l:
        N.append(len(str(abs(i))))
    print(*N)
    
k=int(input())
count(k)