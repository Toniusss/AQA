#  Exercise_1A

str_1 = "James"
new_str = str_1[0], str_1[len(str_1)//2], str_1[-1]
print(*new_str, sep='')


#  Exercise_1B

string = ["JhonDipPeta", "JaSonAy"]
for i in string:
    print(*i[len(i)//2 - 1], i[len(i)//2], i[len(i)//2 + 1], sep='')


#  Exercise_2

s_1 = "Ault"
s_2 = "Kelly"
new_string = s_1[:len(s_1)//2] + s_2 + s_1[len(s_1)//2:]
print(new_string)


#  Exercise_3

s_1 = "America"
s_2 = "Japan"
new_string = s_1[0] + s_2[0] + s_1[len(s_1)//2] + s_2[len(s_2)//2] + s_1[-1] + s_2[-1]
print(new_string)


#  Exercise_4

string = 'PyNaTive'
new_string = [char for char in string if char.islower()] + [char for char in string if char.isupper()]
print(*new_string, sep='')


#  Exercise_5

string = "P@#yn26at^&i5ve"
letters = [char for char in string if char.isalpha()]
digits = [char for char in string if char.isdigit()]
special_symbols = [char for char in string if not char.isalnum() and not char.isspace()]
print(f'Total counts of chars, digits, and symbols:\nLetters - {len(letters)}\nDigits - {len(digits)}\nSpecial symbols - {len(special_symbols)}')


#  Exercise_6

s1 = "Asfapjaspnsas"
s2 = "Xyzfdgh"

if len(s1) > len(s2):
    s3 = s1[len(s2):]
elif len(s1) < len(s2):
    s3 = s2[len(s1):]
else:
    s3 = ''

for i, j in zip(range(len(s1)), reversed(range(len(s2)))):
    print(s1[i], s2[j], sep='', end='')
print(s3, sep='', end='')


#  Exercise_7

def balance_check(string_1, string_2):
    smallest_string, biggest_string = zip(string_2, string_1) if len(string_1) >= len(string_2) else string_1, string_2
    balance_status = True
    for char in smallest_string:
        if char in biggest_string:
            continue
        if char not in biggest_string:
            balance_status = False
            break
    return balance_status


print(balance_check("Yn", "PYnative"))
print(balance_check("Ynf", "PYnative"))


#  Exercise_8

string = "Welcome to USA. usa awesome, isn't it?"
print(f'The USA count is: {string.lower().count("USA".lower())}')


#  Exercise_9

string = "PYnative29@#8496"
numeric_count = [int(char) for char in string if char.isnumeric()]
print(f'Sum: {sum(numeric_count)}, average: {sum(numeric_count) / len(numeric_count)}')


# Exercise_10

str1 = "Apple"

char_dict = dict()

for char in str1:
    count = str1.count(char)
    char_dict[char] = count

print('Result:', char_dict)


# Exercise_11

string = "PYnative"
print(f'Original string is: {string} \nReversed string is: {string[::-1]}')

# or

string = "PYnative"
print(f'\nOriginal string is: {string} \nReversed string is: {''.join(reversed(string))}')


# Exercise_12

string = "Emma is a data scientist who knows Python. Emma works at google."
print(f'Original String is: {string} \nLast occurrence of Emma starts at index: {string.rfind('Emma')}')


# Exercise_13

string = 'Emma-is-a-data-scientist'
print(f"Displaying each substring\n\n{'\n'.join(string.split('-'))}")


# Exercise_14

names_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
print(f'Original list of sting: {names_list}\nAfter removing empty strings: {list(filter(None, names_list))}')


# Exercise_15

string = "/*Jon is @developer & musician"

special_symbols = [char for char in string if not char.isalnum() and not char.isspace()]
ew_string = list(filter(lambda x: x not in special_symbols, string))
print(''.join(ew_string).replace('  ', ' '))


# Exercise_16

string = 'I am 25 years and 10 months old'
new_string = [char for char in string if char.isnumeric()]
print(*new_string, sep='')


# Exercise_17

string = "Emma25 is Data scientist50 and AI Expert"
new_string = [char for char in string.split(' ') if char.isalnum() and not char.isnumeric() and not char.isalpha()]
print(*new_string, sep='\n')


# Exercise_18

string = '/*Jon is @developer & musician!!'
for_removal = list(set(filter(None, [char for char in string if not char.isalnum() and not char.isspace()])))
new_string_1 = ''
for i in string:
    if i in ''.join(for_removal):
        new_string_1 += '#'
    else:
        new_string_1 += i
print(new_string_1)