'''List[] mutable  it can hold Duplicate Values it has Methods Like
 Append It will add Values At Last ,
 Pop() By default It will remove the Last Value
 Sort() it will sort the Collection Of Objects
 clear() this method will clear the list
 insert() this will take two values firstOne is Postion and SecondOne is Object it is Used to Add
 remove() method will remove The Object From the List
 reverse() method will reverse all the Objects

MyList = ['Happy','Ballon','Apple','Iphone','Grapees','Baffallo']
MyList.append("Motrola")
MyList.insert(4,'Bannana')
MyList.sort()
MyList.reverse()
for x in MyList:
'''


'''
dicinory is Key Value Pair key Must All ways String value can be anything that may be set or list or tuple
or Dictonary Also We can access The Value By Calling The Key

dic = {'key1':{'key11':[1,2,3,4,5,6,7]},'key2':("apple","Ball","Cpp","Algorithms","GitHub")}
print(dic['key2'])
print(dic.keys())
print(dic.values())
print(dic.items())

dic2 = {'apple':2.89,'Mango':2.78,'Orange':7.80}
x = input("Enter your Fruit Name to Know the Value")
print(dic2[x])'''


'''Tuple() is dataStructure in Python it is simillar like as list but tuple is immutable and it has
very less methods 
tu = (1,5,3,5,2,5,1,7,9,10)
print(tu.count(5))
print(tu.index(5))'''

'''Set{} it is a immutable and it cannot hold duplicate values'''