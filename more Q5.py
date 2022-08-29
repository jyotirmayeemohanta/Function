def my_function():
    i=int(input("enter any no"))
    fac=1
    while i>0:
        fac=fac*i
        i=i-1
    print("factorial",fac)
my_function()