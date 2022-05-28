n=int(input())
E=0
O=0
M=0
while n:
    if(n%10)%2==0:
        E+=1
    elif(n%10)%2:
        O+=1
    M+=1
    n//=10
if M==E:
    print("Even")
elif M==O:
    print("Odd")
else:
    print("Mixed")