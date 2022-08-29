def f():
    i=0
    a=int(input("enter any no"))
    c=0
    c1=0
    while i<=(a):
        if i%2==0:
            c=c+1
        elif i%2!=0:
            c1=c1+1
        i+=1
    print(c,"ODD")
    print(c1,"EVEN")
f()


