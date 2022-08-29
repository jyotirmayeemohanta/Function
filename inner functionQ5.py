def function(limit):
    global sum1
    sum1 =0
    a=0
    while a <= limit:
        if a % 3 == 0 :
            sum1=sum1+a
        if a % 5 == 0 :
            sum1=sum1+a   
        a+=1
    print(sum1)
function(10)