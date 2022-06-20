h=int(input())
s=0
p=1
while h:
    s+=h%10
    p*=h%10
    h//=10
print(p-s)