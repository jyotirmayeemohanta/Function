# def my_function():
#     list1 = [1, 342, 75, 23, 98]
#     list2 = [75, 23, 98, 12, 78, 10, 1]
#     i=0
#     list3=[]
#     while i<len(list1):
#         if list1[i] in list2:
#             list3.append(list1[i])
#         i+=1
#     print(list3)
# my_function()



list1 = [1,5,10,12,16,20]
list2 = [1,2,10,13,16]
i=0
list3=[]
while i<len(list1) and i<len(list2):
    list2.entend(list1)
    print(list2)
    i+=1
