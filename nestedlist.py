#1
print('='*15,"#1","="*15)
nested1 = [['a','b','c'], ['d','e'],['f','g','h']]
nested1[0].append('z') #I'm adding a new item inside the sublist [0] to the end of the list
nested1[1].append('w') #I'm adding a new item inside the sublist [1] to the end of the list


print(nested1[0])
print(len(nested1))
nested1.append(['i']) #Adds a new list with 'i' to the end of the list
for L in nested1:
    print(L)

#2
print('='*15,"#2","="*15)
nested1 = [['a','b','c'], ['d','e'],['f','g','h']]
y = nested1[1]
print(y) #Just the first sublist
print(y[0]) #Just the first item inside the sublist 

print([10, 20, 30][1]) #Create a lista, and then get the second value from the list created
print(nested1[1][0]) #If there is a list before the square bracket, so Python will understand the 
#first square bracket as an index (He will get the sublist that you called) and another square bracket
#will indicate that you will get something inside that sublist

#3 Change a value inside the sublist and choose the position that you want to change
print('='*15,"#3","="*15)

nested1 = [['a','b','c'], ['d','e'],['f','g','h']]
nested1 [1] = [1, 2, 3 ] #Get the first subslist ['d','e'] and change the value to [1,2,3]
nested1 [1] [0] = 100  #Then change the first value of the new list created before "[1,2,3]" to 100
print(nested1[1])

#4 
print('='*15,"#4","="*15)

nested2 = [{'a': 1, 'b': 3}, {'a':5, 'c':90, 5:50}, {'b':3, 'c':'yes'}]

#5 
print('='*15,"#5","="*15)

data = ['bagel', 'cream cheese', 'breakfast', 'grits', 'eggs', 'bacon', [34, 9, 73, []], [['willow', 'birch', 'elm'], 'apple', 'peach', 'cherry']]
plant = data[7][0][0]
print(plant)

