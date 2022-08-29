def sum(b,c):
    e=b+c
    print(e)
def sub(a,d):
    g=a-d
    print(g)
def mult (s,t):
    u=s*t
    print(u)
def div (q,r):
    m=q/r
    print(m)
def mod(n,p):
    f=n**p
    print(f)
def floor_div(v,w):
    x=v//w
    print(x)
def main_fun( ):
    if op=='+':
        sum(user,user1)
    if op=="-":
        sub(user,user1)
    if op=="*":
        mult(user,user1)
    if op=='/':
        div(user,user1)
    if op=="**":
        mod(user,user1)
    if op=="//":
        floor_div(user,user1)
user=int(input("enter any number"))
user1=int(input("enter your number"))
op=input("entr your singh")
main_fun() 