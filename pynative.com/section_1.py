# Exercise_15

def exponent(base, exp):
    exp_list = []
    for i in range(exp):
        exp_list.append(base)
    calculation_result = base ** len(exp_list)

    lists = []
    for ii in exp_list:
        lists.append(f'{ii} * ')
    explain = ''.join(lists)[:-2]
    return calculation_result, explain


base_value = 2
exp_value = 5
data = exponent(base_value, exp_value)
print(f'{base_value} raises to the power of {exp_value}: {data[0]} i.e. ({data[1]}= {data[0]})')


# Exercise_14


for i in reversed(range(1, 10)):
    print('* ' * i)


# Exercise_13


for i in range(1, 11):
    print(i, ' ', end='')
    for ii in range(2, 11):
        print(i*ii, end=' ')
    print('')


# Exercise_12


# limits in dollars
level_1_limit = 10000
level_2_limit = 10000
# taxes in %
level_1_tax = 0
level_2_tax = 10
level_3_tax = 20

total_yearly_income = 100000


def tax_calc(total_yearly_income_arg):
    if total_yearly_income_arg >= (level_1_limit + level_2_limit):
        level_3_total = total_yearly_income - (level_1_limit + level_2_limit)
        level_3_payment = level_3_total / 100 * level_3_tax
        level_2_payment = level_2_limit / 100 * level_2_tax
        level_1_payment = level_1_limit / 100 * level_1_tax
        sum_of_taxes = sum([level_3_payment, level_2_payment, level_1_payment])
        message = f'Total income: $ {total_yearly_income_arg} \nTotal taxes: $ {round(sum_of_taxes, 2)}'
        return message
    if total_yearly_income_arg < (level_1_limit + level_2_limit):
        if total_yearly_income_arg <= 0:
            message = f'Total income: $ {total_yearly_income_arg} \nTotal taxes: $ 0.0'
            return message
        if total_yearly_income_arg < level_1_limit:
            level_1_payment = total_yearly_income_arg / 100 * level_1_tax
            message = f'Total income: $ {total_yearly_income_arg} \nTotal taxes: $ {round(level_1_payment, 2)}'
            return message
        if total_yearly_income_arg >= level_1_limit:
            level_2_total = total_yearly_income - level_1_limit
            level_2_payment = level_2_total / 100 * level_2_tax
            level_1_payment = level_1_limit / 100 * level_1_tax
            sum_of_taxes = sum([level_2_payment, level_1_payment])
            message = f'Total income: $ {total_yearly_income_arg} \nTotal taxes: $ {round(sum_of_taxes, 2)}'
            return message


print(tax_calc(total_yearly_income))


# Exercise_11


number = 3957
number_list = list(str(number))
print(f'Original number: {number} \nReversed number: {" ".join(list(str(number)[::-1]))}')


# Exercise_10


def sum_of_lists(list_1, list_2):
    list_3 = []
    for number in list_1:
        if number % 2 >= 1:
            list_3.append(number)
    for number in list_2:
        if number % 2 == 0:
            list_3.append(number)
    print(f'Result list: {list_3}')


numbers_list_1 = [10, 20, 25, 30, 35]
numbers_list_2 = [40, 45, 60, 75, 90]
sum_of_lists(numbers_list_1, numbers_list_2)


# Exercise_9


def palindrome_check(numbers):
    print(f'Total of numbers: [{len(numbers)}]: {numbers} \n')
    for index, value in enumerate(numbers):
        reverse_number = str(value)[::-1]
        print(f'[{index+1}] Number: {numbers[index]}, reversed: {reverse_number}')
        if value == int(reverse_number):
            print(f'Palindrome: {True}')
        else:
            print(f'Palindrome: {False}')


numbers = [123, 909, 931, 999, 100]
palindrome_check(numbers)


# Exercise_8


range_of_numbers = range(1, 6)
for i in range_of_numbers:
    for count_of_repeat in range(i):
        print(i, end=' ')
    print('')


# or


for i in range(1, 6):
    print(f'{i} ' * i)


# Exercise_7


string = "Emma is good developer. Emma is a writer"
substring = 'Emma'

def check_count_of_substring(substring):
    return string.count(substring)
    # return len(string.split(substring)) - 1


print(f"String: {string}")
print(f"Substring: {substring}")
print(f"Count of a given substring: {check_count_of_substring(substring)}")


# Exercise_6

data = [10, 20, 33, 46, 55]
divider = 5
print(f'Data: {data} \nDivisible by {divider}:')

for i in data:
    if i % divider == 0:
        print(i)


# Exercise_5


def same_check(numbers_list):
    print('Data:', *numbers_list)

    if numbers_list[0] == numbers_list[-1]:
        print(f'First and last numbers is same: {True}')
    else:
        print(f'First and last numbers is same: {False}')


numbers_x = [10, 20, 30, 40, 10]
same_check(numbers_x)
print('')
numbers_y = [75, 65, 35, 75, 30]
same_check(numbers_y)


# Exercise_4


def remove_chars(word, number):
    return word[number:]

print(remove_chars("random word", 1))
print(remove_chars("random word", 3))
print(remove_chars("random word", 4))
print(remove_chars("random word", 7))


# Exercise_3


word = 'pynative'
for i in range(len(word)):
    if i % 2 == 0:
        print(f'{word[i]}')
    else:
        pass


# Exercise_2


print('Printing current and previous number and their number and their sin in a range(10)')
previous_num = 0

for i in range(1, 11):
    x_sum = previous_num + i
    print(f'Current number: {i}, previous number: {previous_num}, sum: {x_sum}')
    previous_num = i


# Exercise_1


def calculation(a, b):
    mult = a * b
    if mult <= 1000:
        return mult
    else:
        adding = a + b
        return adding


number_1 = 30
number_2 = 30
print(f'The result is: {calculation(number_1, number_2)}')