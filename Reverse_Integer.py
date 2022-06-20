l=int(input())
rev=0
if l>0:
    while l:
        rev=rev*10+l%10
        l//=10
        if l==0:
            print(rev)
else:
    l*=-1
    while l:
        rev=rev*10+l%10
        l//=10
        if l==0:
            rev=str(rev)
            print("-"+rev)