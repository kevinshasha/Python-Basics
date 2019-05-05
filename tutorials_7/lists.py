def createList():
    lst = [1, 2, 3, 4]
    return lst

def printnums(lst):
    for n in lst: 
        print(n)

def appendlist(lst, n):
    lst.append(n)

def propendlist(lst,n):
    lst.insert(0,n)

def linearsearch(lst, n):
    pos=0
    for item in myList:
        if item !=n: 
            pos+=1
        if item==n: 
            return pos
    return -1
    
    
if __name__== '__main__':
    myList = ['a','b','c','d','e']
    print(myList)
    x=linearsearch(myList, 'e')
    print(x)