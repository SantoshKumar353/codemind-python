k=int(input())
rev=0
temp=k
while temp:
    rev=rev*10+temp%10
    temp//=10
if rev==k:
    print(True)
else:
    print(False)