def speed():
    num=int(input("enter any no"))
    if num<70:
        print("ok")
    elif num==80:
        print("point2")
    elif num>70 and num<135:
        print(num+5,"point1")
    else:
        print("licence suspended")
speed()