kumar=input("enter your gasssing option")
jyoti=input("enter your gassing option")
if kumar=="rock"and jyoti=="rock"or kumar=="paper"and jyoti=="paper"or kumar=="scissors"and jyoti=="scissors":
    print("Game withdrow")
elif kumar=="rock"and jyoti=="paper"or kumar=="paper"and jyoti=="scissors"or kumar=="scissors"and jyoti=="rock":
    print("jyoti 1 point")
elif kumar=="rock"and jyoti=="scissors"or kumar=="scissors"and jyoti=="papers"or kumar=="papers"and jyoti=="rock":
    print("kumar 1 point")