# Link to exercises: https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/



# Exercise_1

counter = 1
while counter <= 10:
    print(counter)
    counter += 1


# Exercise_2

num_list = []
for i in range(1, 10):
    num_list.append(i)
    print(*num_list)


# Exercise_3

print(sum(range(1, int(input('Enter number here: ')) + 1)))


# Exercise_4

n = 2
for i in range(1, 11):
    print(n * i)


# Exercise_5

numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if i > 500:
        break
    if i > 150:
        continue
    if i % 5 != 0:
        continue
    else:
        print(i)


# Exercise_6

n = 75869
counter = 0
numbers_list = []
while n != 0:
    try:
        numbers_list.append((str(n)[counter]))
        counter += 1
    except IndexError:
        break
print(len(numbers_list))


# Exercise_7

for i in reversed(range(1, 6)):
    for ii in reversed(range(i)):
        print(f'{ii+1} ', end='')
    print(' ')

# or

# n = 5
# k = 5
# for i in range(0,n+1):
#     for j in range(k-i,0,-1):
#         print(j,end=' ')
#     print()


# Exercise_8

list1 = [10, 20, 30, 40, 50]
for i in reversed(list1):
    print(i)


# Exercise_9

for i in range(-10, 0):
    print(i)


# Exercise_10

for i in range(5):
    print(i)
else:
    print('Done!')


#  Exercise_11

start = 25
end = 50
print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    if num > 1:
        # removed unnecessary values using int(num**0.5)
        for i in range(2, int(num**0.5) + 1):
            if (num % i) == 0:
                break
        else:
            print(num)


#  Exercise_12

num_1, num_2 = 0, 1
for i in range(10):
    result = num_1 + num_2
    print(result)
    num_1 = num_2
    num_2 = result


#  Exercise_13

num = 5
factorial = 1
if num < 0:
    print('Number < 0')
elif num == 0:
    print('Number = 0')
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print(f'The factorial of {num}: {factorial}')


#  Exercise_14

num = 76542
for i in reversed(list(str(num))):
    print(i, end='')


#  Exercise_15

num_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in range(len(num_list)):
    odd_check = i + 1
    if odd_check % 2 != 0:
        continue
    else:
        print(f'{num_list[i]} ', end="")

# or

print(' ')
for i in num_list[1::2]:
    print(i, end=" ")


#  Exercise_16

input_number = 6

for i in range(1, input_number + 1):
    print(f'Current number is: {i}, and the cude is: {i ** 3}')


#  Exercise_17

n = 5
num_list = []
for i in range(1, n + 1):
    num_list.append(int('2' * i))
print(sum(num_list))


#  Exercise_18

for i in range(1, 6):
    print('* ' * i)
for i in reversed(range(1, 5)):
    print('* ' * i)




