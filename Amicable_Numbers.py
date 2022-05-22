i=int(input())
j=int(input())
x=1
sum=0
while x<=i//2:
    if i%x==0:
        sum+=x
    x+=1
if sum==j:
    print("Amicable")
else:
    print("Not Amicable")