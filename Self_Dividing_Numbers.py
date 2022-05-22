s=int(input())
n=int(input())
while s!=n+1:
    temp=s
    c=0
    f=0
    while temp%10!=0:
        d=temp%10
        temp//=10
        if s%d==0:
            c+=1
        f+=1
    if c==f and s%10!=0:
        print(s,end=' ')
    s+=1