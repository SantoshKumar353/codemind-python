t=int(input())
fact=0
x=1
while x<=t//2:
    if t%x==0:
        fact+=x
    x+=1
if fact>t:
    print(True)
else:
    print(False)