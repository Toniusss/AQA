import os

# Exercise_1

number_1 = input('Enter first number here: ')
number_2 = input('Enter second number here: ')
result = int(number_1) * int(number_2)
print(result)


# Exercise_2

print('Name', 'Is', 'James', sep='**')


# Exercise_3

num = 8
print('%o' % num)


# Exercise_4

num = 458.541315
print('%.2f' % num)
# print(round(num, 2))


# Exercise_5

numbers_list = []
for i in range(5):
    data = float(input('Enter number here: '))
    numbers_list.append(data)
print(numbers_list)


# Exercise_6

with open('text.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

with open('text_new.txt', 'w') as file:
    count = 0
    for line in lines:
        if count == 4:
            count += 1
            continue
        else:
            file.write(line)
        count += 1

# check
with open('text_new.txt', 'r') as file:
    lines = file.readlines()
    print(lines)


# Exercise_7

data = input('Enter three names, separated by a space: ').split()
for i, counter in zip(data, range(len(data))):
    print(f'Name {counter+1}: {i}')


# Exercise_8

totalMoney = 1000
quantity = 2
price = 450

print(f'I have {totalMoney} dollars, so I can buy {quantity} football for {round(price, 2)} dollars.')

statement1 = "I have {1} dollars, so I can buy {0} football for {2:.2f} dollars."
print(statement1.format(quantity, totalMoney, price))


# Exercise_9

size = os.stat('text.txt').st_size
# size = 0
if size == 0:
    print('File is empty')
else:
    print(f'File is not empty. Size: {size}')


# Exercise_10

with open('text.txt', 'r') as file:
    lines = file.readlines()
    print(lines[3])
