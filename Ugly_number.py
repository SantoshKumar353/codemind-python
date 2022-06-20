k=int(input())
x=0
while k!=1:
    if k%2==0:
        k//=2
    elif k%3==0:
        k//=3
    elif k%5==0:
        k//=5
    else:
        x+=1
        break
if x==0:
    print("Ugly Number")
else:
    print("Not Ugly Number")