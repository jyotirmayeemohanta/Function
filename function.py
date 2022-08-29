list1=[1,5,10,12,16,20]
list2=[1,2,10,13,16]
def function(list1,list2):
    i=0
    a=[]
    b=list(list1)
    c=list(list2)
    while i<len(list2):
        if list2[i] in list1:
            if list2[i] not in a:
                a.append(list2[i])
        i+=1
    print(a)
function(list1,list2)