a=input()
if(a[0:2]=="00"):
    print("12"+":"+a[3:5],"AM")
elif int(a[0:2])<12:
    print(a[0:2]+":"+a[3:5],"AM")
elif int(a[0:2])==12:
    print(a[0:2]+":"+a[3:5],"PM")
elif int(a[0:2])>12:
    k=int(a[0:2])-12
    if k<10:
        print("0"+str(k)+":"+a[3:5],"PM")
    else:
        print(str(k)+":"+a[3:5],"PM")