#  Exercise_1

list_1 = [3, 6, 9, 12, 15, 18, 21]
list_2 = [4, 8, 12, 16, 20, 24, 28]

new_list_1 = list_1[1::2]
new_list_2 = list_2[::2]
final_list = new_list_1 + new_list_2

print(final_list)


#  Exercise_2

num_list = [54, 44, 27, 79, 91, 41]
print(f'{num_list} - origin')
for_removal = num_list[4]
num_list.pop(4)
print(f'{num_list} - after removal the number [{for_removal}] by index [4]')
num_list.insert(2, for_removal)
print(f'{num_list} - after adding the number [{for_removal}] by index [2]')

num_list.append(for_removal)
print(f'{num_list} - after adding the number [{for_removal}] at the end')


#  Exercise_3

num_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
one_part = int(len(num_list) // 3)


def make_parts(num_list):
    return num_list[:one_part], num_list[one_part:one_part * 2], num_list[one_part * 2:]


result = make_parts(num_list)
print(f'{num_list}\n{result[0]} - {result[0][::-1]}\n{result[1]} - {result[1][::-1]}\n{result[2]} - {result[2][::-1]}\n ')


#  Exercise_4

num_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

char_dict = dict()

for char in num_list:
    count = num_list.count(char)
    char_dict[char] = count

print('Result:', char_dict)


#  Exercise_5

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

lists_addition = set(zip(first_list, second_list))
print(lists_addition)


# Exercise_6

set_1 = {23, 42, 65, 57, 78, 83, 29}
set_2 = {57, 83, 29, 67, 73, 43, 48}

common_elements = set(set_1) & set(set_2)
# common_set = set.union(set(set_1), set(set_2))
final_set = [item for item in set_1 if item not in common_elements]

print(common_elements)
print(set(final_set))


#  Exercise_7

set_1 = {27, 43, 34}
set_2 = {34, 93, 22, 27, 43, 53, 48}

print(f'First set is subset of second set - {set_1.issubset(set_2)}')
print(f'Second set is subset of First set - {set_2.issubset(set_1)}\n')

print(f'First set is Super set of second set - {set_1.issuperset(set_2)}')
print(f'Second set is Super set of First set - {set_2.issuperset(set_1)}\n')

if set_1.issubset(set_2):
    set_1.clear()
if set_2.issubset(set_1):
    set_2.clear()

print(f'First Set - {set_1}')
print(f'Second Set - {set_2}')


# Exercise_8

age_list = [47, 64, 69, 37, 76, 83, 95, 97]
name_age_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

age_list[:] = [item for item in age_list if item in name_age_dict.values()]
print(f'After removing unwanted elements from list - {age_list}')


# Exercise_9

speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
print(list(set(speed.values())))


#  Exercise_10

num_list = [87, 45, 41, 65, 94, 41, 99, 94]
num_set = set(num_list)
print(f'Unique items: {num_set}')
num_tuple = tuple(num_set)
print(f'Tuple : {num_set}')
print(f'Min : {min(num_tuple)}')
print(f'Max : {max(num_tuple)}')
