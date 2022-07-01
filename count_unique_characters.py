def co_char(n):
    n=n.replace(" ","")
    c=0
    for i in n:
        if n.count(i)==1:
            c+=1
    print(c)
    
n=input().lower()
co_char(n)