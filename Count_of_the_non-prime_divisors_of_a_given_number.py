def is_prime(k):
    for i in range(2,(k//2)+1):
        if k%i==0:
            return 0
    return 1
    
k=int(input())
c=2
for i in range(2,(k//2)+1):
    if k%i==0:
        if is_prime(i):
            i+=1
            continue
        else:
            c+=1
print(c)