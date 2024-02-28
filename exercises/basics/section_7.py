#  Exercise_1

num_list = [100, 200, 300, 400, 500]
print(num_list[::-1])


#  Exercise_2

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

result = []

for i in range(len(list1)):
    result.append(list1[i] + list2[i])
print(result)


#  Exercise_3

numbers = [1, 2, 3, 4, 5, 6, 7]
print([item * item for item in numbers])


#  Exercise_4

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

print([x + y for x in list1 for y in list2])


# Exercise_5

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, reversed(list2)):
    print(x, y)


#  Exercise_6

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
print(list(filter(None, list1)))


#  Exercise_7

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)


#  Exercise_8

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]
list1[2][1][2].extend(sub_list)
print(list1)


#  Exercise_9

list1 = [5, 10, 15, 20, 25, 50, 20]
list1[list1.index(20)] = 200
print(list1)


#  Exercise_10

list1 = [5, 20, 15, 20, 25, 50, 20]
print([x for x in list1 if x != 20])
