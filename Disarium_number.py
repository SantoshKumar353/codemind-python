o=int(input())
temp=o
d=0
while temp:
    d+=1
    temp//=10
number=o
sum=0
while o:
    sum+=(o%10)**d
    o//=10
    d-=1
if sum==number:
    print(True)
else:
    print(False)