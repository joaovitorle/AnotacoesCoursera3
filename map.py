#1 Manual way
print('='*15,"#1","="*15)

def doubleStuff(a_list):
    #return a new list in which contains doubles of the elements is a_list.
    new_list = []
    for value in a_list:
        new_element = 2* value
        new_list.append(new_element)
    return new_list

things = [2,5,9]
print(things)
things = doubleStuff(things)
print(things)

#2
print('='*15,"#2","="*15)

def triple(value): #Crate a function which takes some unknown value and multiply by 3
    return 3*value

def tripleStuff(a_list):
    new_list = map(triple, a_list) #The map function apply the transformation occured in function triple
    #and apply to every single item in the a_list
    return new_list

def quadrupleStuff(a_list):
    new_list = map(lambda value:4*value, a_list) #Instead we creat a new function very similar to triple
    #which gonna take some unknown value and multiply by 4, we just use lambda, which calls a parameter "value"
    #and multiply by 4 and apply this "function" to all items in a_list
    return new_list

things = [2, 5, 9]
things3 = list(tripleStuff(things)) #We need to put map into a list to avoid error
print (things3)
things4 = list(quadrupleStuff(things)) 
print(things4)


#3 
print('='*15,"#3","="*15)
abbrevs = ['usa','esp','chn','jpn','mex','can','rus','rsa','jam']

def abbrevscaptalized (up):
    return up.upper()

abbrevs_upper = list(map(abbrevscaptalized ,abbrevs))

print(abbrevs_upper)