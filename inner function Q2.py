# num=int(input("enter any no"))
# start=1
# count=0
# while start<=num:
#     if num%start==0:
#         count+=1
#     start+=1
# if count==2:
#     print("prime no")
# else:
#     print("not prime no")


# num=int(input("enter any no"))
# i=1
# sum=0
# while i<=num:
#     if num%i==0:
#         sum=sum+i
#     i=i+1
#     if i==sum:
#         print(num,"perfect no")
#     else:
#         print(num,"not perfect no")

num=int(input("enter a no"))
i=1
c=0
while i<=num:
    if num%2==0:
        c=c+1
    i=i+1
if c==num:
    print("perfect no")
else:
    print("not perfect no")