#  Exercise_1

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
print(dict(zip(keys, values)))


#  Exercise_2

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3 = dict1 | dict2
print(dict3)


#  Exercise_3

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

print(sampleDict['class']['student']['marks']['history'])


#  Exercise_4

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

print(dict.fromkeys(employees, defaults))


#  Exercise_5

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

keys = ["name", "salary"]

my_dict = {key: sample_dict[key] for key in keys}
print(my_dict)


#  Exercise_6

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

keys = ["name", "salary"]

for key in keys:
    del sample_dict[key]
print(sample_dict)


#  Exercise_7

sample_dict = {'a': 100, 'b': 200, 'c': 300}
if 200 in sample_dict.values():
    print('200 present in a dict')


# Exercise_8

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

sample_dict.update({'location': sample_dict.pop("city")})
# sample_dict['location'] = sample_dict.pop('city')
print(sample_dict)


#  Exercise_9

sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

print(f'{min(sample_dict, key=sample_dict.get)}: {min(sample_dict.values())}')


#  Exercise_10

sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

sample_dict['emp3']['salary'] = 8500
print(sample_dict)

