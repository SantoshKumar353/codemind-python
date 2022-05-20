oct=int(input())
dec=0
i=0
bin=0
while (oct!=0):
    dec=dec+(oct%10)*pow(8,i)
    i+=1
    oct//=10
i=1
while(dec!=0):
    bin=bin+(dec%2)*i
    dec//=2
    i=i*10
print(bin)