#  Exercise_1

def func(name_value, age_value):
    print(f'Name: {name_value}, age: {age_value}')


func('Tom', 30)


#  Exercise_2

def func(*args):
    print('Arguments:')
    for i in args:
        print(i)


func(20, 40, 60)
func(80, 100)


#  Exercise_3

def calculation(a, b):
    return a + b, a - b


a, b = 40, 10
print(f'Numbers: {a}, {b} \nAddition: {calculation(a, b)[0]} \nSubtraction: {calculation(a, b)[1]}')


#  Exercise_4

def show_employee(name, salary=9000):
    return print(f'Name: {name}, salary: {salary}')


show_employee("Ben", 12000)
show_employee("Jessa")


#  Exercise_5

def calc(a_outer, b_outer):
    def addition(a_inner, b_inner):
        return a_inner + b_inner
    return addition(a_outer, b_outer) + 5


print(calc(5, 10))


#  Exercise_6

def calc():
    sum_list = []
    for i in range(1, 11):
        sum_list.append(i)
    return sum(sum_list)


print(calc())


#  Exercise_7

def display_student(name, age):
    print(name, age)


display_student('Hanna', 19)
new_name = display_student
new_name('John', 32)


#  Exercise_8

def even_numbers():
    numbers_list = []
    for i in range(4, 30)[::2]:
        numbers_list.append(i)
    return numbers_list


print(even_numbers())

# or

print(list(range(4, 30, 2)))


#  Exercise_9

x = [4, 6, 8, 24, 12, 2]
print(sorted(x)[-1],)
# or
print(sorted(x, reverse=True)[0])

