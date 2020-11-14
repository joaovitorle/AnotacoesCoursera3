print('='*15,"#1","="*15)
#1
nested1 = [['a','b','c'],['d','e'],['f','g','h']]
for x in nested1:
    print('level1: ')
    for y in x:
        print("   level2: " +y)

print('='*15,"#2","="*15)
#2
info = [['Tina', 'Turner', 1939, 'singer'], ['Matt', 'Damon', 1970, 'actor'], ['Kristen', 'Wiig', 1973, 'comedian'], ['Michael', 'Phelps', 1985, 'swimmer'], ['Barack', 'Obama', 1961, 'president']]
last_names = [] #Accumulator
for x in info:
    last_names.append(x[1]) #Incluir dentro da lista, na última posição, o último nome
    print(last_names)

print('='*15,"#3","="*15)
#3
info = [['Tina', 'Turner', 1939, 'singer'], ['Matt', 'Damon', 1970, 'actor'], ['Kristen', 'Wiig', 1973, 'comedian'], ['Michael', 'Phelps', 1985, 'swimmer'], ['Barack', 'Obama', 1961, 'president']]
for x in info:
    for val in x:
        print(val) #To extract all the values into the lists

print('='*15,"#4","="*15)
#4 To accumulate a specific value
L = [['apples', 'bananas', 'oranges', 'blueberries', 'lemons'], ['carrots', 'peas', 'cucumbers', 'green beans'], ['root beer', 'smoothies', 'cranberry juice']]
b_string = []

for x in L: #This will get all the sublists in the mainlist
    for y in x: #This will get all the values in the sublists in the mainlists.Ex: apples,bananas,...,cucumbers,... 
        if 'b' in y:
            b_string.append(y) #Coloca dentro da nova lista, na última posição
print(b_string)

print('='*15,"#5","="*15)
#5 Structuring Nested data
nested1 = [1,2,['a','b','c'],['d','e'],['f','g','h']]
for x in nested1:
    print('level1: ')
    if type(x) is list: 
        for y in x:
            print(f'level2: {y}')
    else: #Se não for uma sublista dentro da lista, ou seja um valor inteiro, apenas printa o valor
        print(x)

print('='*15,"#6","="*15)
#6 Deep and Shallow Copies

original = [['dogs','puppies'],['cats','kittens']]
copied_version = original[:] #To copy all the sublists
print(copied_version)
print(copied_version is original)
print(copied_version == original)
original[0].append(['canines'])
print(original)
print('-----Now look at the copied version------')
print(copied_version)

print('='*15,"#7","="*15)
#7 Deep and Shallow Copies
original = [['dogs','puppies'],['cats','kittens']]
copied_outer_list = []
for inner_list in original: #This will get all the sublists in the mainlist
    copied_inner_list = [] #Has created a new list
    for item in inner_list: #This will get all the values in the sublists in the mainlists.
        copied_inner_list.append(item) #Add into the copied_inner_list the values from item, all the values into the main list
    copied_outer_list.append(copied_inner_list) #Add into the copied_outer_list the values from copied_inner_list, all the values into the main list
print(copied_outer_list)
print(copied_inner_list)
original[0].append(['canines'])
print(original)
print('-----Now look at the copied version------')
print(copied_outer_list)
print(copied_inner_list)

print('='*15,"#8","="*15)

#8
import copy
original = [['canines', ['dogs', 'puppies']], ['felines', ['cats', 'kittens']]]
shallow_copy_version = original[:]
deeply_copied_version = copy.deepcopy(original)
original.append("Hi there")
original[0].append(["marsupials"])
print("-------- Original -----------")
print(original)
print("-------- deep copy -----------")
print(deeply_copied_version)
print("-------- shallow copy -----------")
print(shallow_copy_version)

#9 A worked example of nested iteration
print('='*15,"#9","="*15)

big_list = [[['one','two',],['seven','eight']],[['nine','four']],[['three','one']]]


word_counts = {}

for sub1 in big_list:
    for sub2 in sub1:
        for word in sub2:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

print(word_counts)
