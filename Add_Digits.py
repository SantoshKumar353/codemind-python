l=int(input())
sum=0
while 1:
    if l==0 and sum>9:
        l=sum
        sum=0
    elif l==0 and sum<10:
        print(sum)
        break
    sum+=l%10
    l//=10