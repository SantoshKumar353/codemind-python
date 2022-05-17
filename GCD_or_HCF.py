def hcf_gcd(a,b):
    if a>b:
        max=a
    else:
        max=b
    while True:
        if a%max==0 and b%max==0:
            return max
        max-=1
a,b=map(int,input().split())
s=hcf_gcd(a,b)
print(s)