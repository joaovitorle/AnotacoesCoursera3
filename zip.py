#1 Interation through lists
L1 = [3,4,5]
L2 = [1,2,3]
L3 = []

for i in range(len(L1)):
    L3.append(L1[i] + L2[i])

print(L3)

#2 
L1 = [3,4,5]
L2 = [1,2,3]
L4 = list(zip(L1,L2)) #The zip fuction takes two or more sequences and it makes a list of tuples
print(L4)

#3
L1 = [3,4,5]
L2 = [1,2,3]
L3 = []
L4 = list(zip(L1,L2)) #The zip fuction takes two or more sequences and it makes a list of tuples

for (x1,x2) in L4:
    L3.append(x1+x2)
print(L3)

#4
L1 = [3,4,5]
L2 = [1,2,3]
L3 = [x1 + x2 for (x1,x2) in list(zip(L1, L2))]
print(L3)

