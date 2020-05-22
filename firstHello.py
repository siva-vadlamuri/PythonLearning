'''List [] it is mutable  we can add duplicates'''
'''Set {} it is imutable and it does not hold any duplicates'''
'''tuple () its a imutable Once assigned cannot change and it can hold duplicates '''
'''Dictonary key:Value pair{}'''
'''Python is dynamic typing language'''
'''Bodmas rule
Strings -->indexing[0] and Slicing[1:15] or [1:15:2] firstOne is inclusive secondOne is Exclusive 
thirdOne is Step to jump

shivaa = "My Name is shiva"
ss = ""
for x in range(5):
    for y in  x:
        print(y)
    print(end="")
x = shivaa[-2]
y = shivaa[1:4]
print(x)
print(y)
print(len(shivaa))'''
'''fruits = ["apple","Mango","Orange","Pinapple"]
fruits[1] = "Gauva"
for x in fruits:
    print(x)

print("--------------------------------------Set-------------------------------------------")
animals = {"tiger","peacock","Lion","tiger"}
for y in animals:
    print(y)
print("<--------------------tuple----------------------------------------------------->")
shiva = ("hello",123,12.0,"apple",0,"hello")
for z in shiva:
    print(z)'''
'''for x in range(100):
    if(x%2==0):
        print(f"{x} is a Even Number")
    else:
        print(f"{x} is odd")
shivaa = "My Name is shiva"
y = shivaa[1:10:2]
print(y)'''
string = 'hello world bujji'
print(string.split(' '))

