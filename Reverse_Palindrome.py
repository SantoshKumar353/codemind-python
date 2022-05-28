def rev_pal(a):
    r=0
    while a:
        r=r*10+a%10
        a//=10
    return r

a=int(input())
while a:
    a+=rev_pal(a)
    if rev_pal(a)==a:
        print(a)
        break