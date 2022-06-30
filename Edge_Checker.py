c,d=map(int,input().split())
if (c==1 and d==10) or(c==10 and d==1):
    print("Yes")
elif c<10 and d<10:
    if c==d+1 or d==c+1:
        print("Yes")
    else:
        print("No")
else:
    print("No")