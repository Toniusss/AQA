#  Exercise_1

set_1 = {"Yellow", "Orange", "Black"}
list_1 = ["Blue", "Green", "Red"]

set_1.update(list_1)

print(set_1)


#  Exercise_2

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.intersection(set2))


#  Exercise_3

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.union(set2))


#  Exercise_4

set1 = {10, 20, 30}
set2 = {20, 40, 50}

print(set1 - set2)


#  Exercise_5

set1 = {10, 20, 30, 40, 50}
set1.difference_update({10, 20, 30})
print(set1)


#  Exercise_6

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.symmetric_difference(set2))


#  Exercise_7

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

set3 = set1 & set2
print(set3)

# or

if set1.isdisjoint(set2):
    print("Two sets have no items in common")
else:
    print("Two sets have items in common")
    print(set1.intersection(set2))


#  Exercise_8

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1.symmetric_difference_update(set2)
print(set1)


#  Exercise_9

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1.intersection_update(set2)
print(set1)


