def u_char(n):
    for i in range(0,len(n)):
        c=n.count(n[i])
        if c==1:
            print(n[i])
            break
    else:
        print('-1')
        
n=input()
u_char(n)