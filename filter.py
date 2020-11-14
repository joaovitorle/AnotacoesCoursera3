#1 Manual way
def keep_evens (nums):
    new_list = []
    for num in nums:
        if num % 2 == 0:
            new_list.append(num)
    return new_list

print(keep_evens([3, 4, 6, 7, 0, 1]))

#2
def keep_evens(nums): 
    new_seq = filter(lambda num: num %2 ==0, nums) #Instead of transforming an input like in map function
    #in filter function we are not transforming, we are just making a binary decision. So, the first parameter
    #is true or false ? if it's true we get if it's false we filtered out
    return list(new_seq)
print(keep_evens([3, 4, 6, 7, 0, 1]))

#3
lst = ['witch','halloween','pumpkin','cat','candy','wagon','moon']

lst2 = list(filter(lambda word: 'o' in word, lst)) 

print(lst2)