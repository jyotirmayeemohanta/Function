string_list = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]
def list():
    i=0
    a=[]
    while i<len(string_list):
        j=0
        while j<len(string_list):
            if string_list[i] not in a:
                a.append(string_list[i])
            j+=1
        i+=1
    print(a)
list()

string_list = ["Delhi", "Delhi", "Mumbai", "Mumbai", "Delhi", "Chennai", 'Chennai']
def list():
    i=0
    a=[]
    while i<len(string_list):
        j=0
        while j<len(string_list):
            if string_list[i] not in a:
                a.append(string_list[i])
            j+=1
        i+=1
    print(a)
list()