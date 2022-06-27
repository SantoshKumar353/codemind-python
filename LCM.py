k, l=map(int,input().split())
i=1
while 1:
    if (k*i)%l==0:
        print(k*i)
        break
    i+=1