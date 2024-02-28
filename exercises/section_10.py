# Exercise_1

tuple1 = (10, 20, 30, 40, 50)
print(tuple1[::-1])


# Exercise_2

tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])


# Exercise_3

tuple_1 = (50, )
print(tuple_1)


# Exercise_4

tuple1 = (10, 20, 30, 40)
for i in tuple1:
    print(i)

# or

a, b, c, d = tuple1
print('\n', a, sep='')
print(b)
print(c)
print(d)



# Exercise_5

tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1, tuple2 = tuple2, tuple1
print(tuple2)
print(tuple1)


# Exercise_6

tuple1 = (11, 22, 33, 44, 55, 66)
tuple2 = tuple1[3:5]
print(tuple2)


# Exercise_7

tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print(tuple1)


# Exercise_8

tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
tuple1 = tuple(sorted(list(tuple1), key=lambda x: x[1]))
print(tuple1)


# Exercise_9

tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))


# Exercise_10

tuple1 = (45, 45, 45, 45)
all_equal = all(x == tuple1[0] for x in tuple1)
print(all_equal)
