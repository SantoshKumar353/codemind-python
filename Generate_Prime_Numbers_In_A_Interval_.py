g=int(input())
h=int(input())
while g<=h:
    c=0
    x=1
    while x<=g//2:
        if g%x==0:
            c+=1
        x+=1
    if c==1:
        print(g)
    g+=1