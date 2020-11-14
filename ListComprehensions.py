#1
things = [2, 5, 9]
yourlist = [value *2 for value in things] #[<transformer_expression> for <variable_name> in <sequence>]

print(yourlist)

#2 Using Comprehension to filtering
def keep_evens(nums):
    new_list = [num for num in nums if num %2 == 0] #[<transformer_expression> for <variable_name> in <sequence> if <filtration_expression>]
    return new_list
print(keep_evens([3,4,6,7,0,1]))

#3
tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}

inner_list = tester['info']
compri = [d['name'] for d in inner_list]
print(compri)

