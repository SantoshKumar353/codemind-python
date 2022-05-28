def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
j=int(input())
p=0
while n<=j:
    if prime(n):
        p+=1
    n+=1
print(p)
        