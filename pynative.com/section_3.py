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

