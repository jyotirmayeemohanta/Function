
a=int(input("Enter any no"))
i=0
b=0
while a>0:
    b=a%10
    i=(i*10)+b
    a=a//10
if a==i:
    print("Palindrome  no")
else:
    print("not palindrome no")
