print('='*15,"#1","="*15)
#1
nested = [['dog', 'cat', 'horse'], ['frog', 'turtle', 'snake', 'gecko'], ['hamster', 'gerbil', 'rat', 'ferret']]

output = nested[1][2] 
print(output)


print('='*15,"#2","="*15)
#2
lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10], ['green', 'yellow', 'purple', 'red']]

for sub1 in lst:
    if 'yellow' in sub1:
        yellow = True
    elif 4 in sub1:
        four = True
    elif 'orange' in sub1:
        orange = True
    else: 
        yellow = False
        four = False
        organge = False
print(yellow)
print(four)
print(orange)

print('='*15,"#3","="*15)
#3
L = [[5, 8, 7], ['hello', 'hi', 'hola'], [6.6, 1.54, 3.99], ['small', 'large']]
test1 = 'hola' in L
# Test if [5, 8, 7] is in the list L. Save to variable name test2
test2 = [5, 8, 7] in L
# Test if 6.6 is in the third element of list L. Save to variable name test3
test3 = 6.6 in L[2]

print(test1)
print(test2)
print(test3)

print('='*15,"#4","="*15)
#4

nested = {'data': ['finding', 23, ['exercises', 'hangout', 34]], 'window': ['part', 'whole', [], 'sum', ['math', 'calculus', 'algebra', 'geometry', 'statistics',['physics', 'chemistry', 'biology']]]}

if 'data' in nested:
    data = True
else: 
    data = False

if 24 in nested:
    twentyfour = True
else:
    twentyfour = False
print(twentyfour)

if 'whole' in nested:
    whole = True
else:
    whole = False

if 'physics' in nested:
    physics = True
else:
    physics = False


print('='*15,"#5","="*15)
#5

nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}

london_gold = nested_d['London']['Great Britain']
print(london_gold)


print('='*15,"#6","="*15)
#6

sports = {'swimming': ['butterfly', 'breaststroke', 'backstroke', 'freestyle'], 'diving': ['springboard', 'platform', 'synchronized'], 'track': ['sprint', 'distance', 'jumps', 'throws'], 'gymnastics': {'women':['vault', 'floor', 'uneven bars', 'balance beam'], 'men': ['vault', 'parallel bars', 'floor', 'rings']}}

# Assign the string 'backstroke' to the name v1
v1 = sports['swimming'][2]
# Assign the string 'platform' to the name v2
v2 = sports['diving'][1]
# Assign the list ['vault', 'floor', 'uneven bars', 'balance beam'] to the name v3
v3 = sports['gymnastics']['women']
# Assign the string 'rings' to the name v4
v4 = sports['gymnastics']['men'][3]

print('='*15,"#7","="*15)
#7
nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}

US_count = []


c1 = nested_d['Beijing']['USA']
c2 = nested_d['London']['USA'] 
c3 = nested_d['Rio']['USA']

US_count.append(c1)
US_count.append(c2)
US_count.append(c3)

print(US_count)


print('='*15,"#8","="*15)
#8
l_of_l = [['purple', 'mauve', 'blue'], ['red', 'maroon', 'blood orange', 'crimson'], ['sea green', 'cornflower', 'lavender', 'indigo'], ['yellow', 'amarillo', 'mac n cheese', 'golden rod']]

third = [i[2] for i in l_of_l]
print(third)

print('='*15,"#9","="*15)
#9

athletes = [
    ['Phelps', 'Lochte', 'Schooling', 'Ledecky', 'Franklin'], 
    ['Felix', 'Bolt', 'Gardner', 'Eaton'], 
    ['Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak', 'Dalton']
]

t = []
other = []

for list in athletes:
    for char in list:
        if 't' in char:
            t.append(char)
        else:
            other.append(char)