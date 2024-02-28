import math
from datetime import date
import random


# Exercise_1

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return round(math.pi * self.radius ** 2, 2)

    def calculate_perimeter(self):
        return round(2 * math.pi * self.radius, 2)


radius = float(input("Input the radius of the circle: "))
circle = Circle(radius)
print(f'Radius: {radius}, area: {Circle(radius).calculate_area()}, perimetr: {Circle(radius).calculate_perimeter()}')


# Exercise_2

class Person():
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def get_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        if today < date(today.year, self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age


person_1 = Person("Ferdi Odilia", "France", date(1962, 7, 12))
person_2 = Person("Shweta Maddox", "Canada", date(1982, 10, 20))
person_3 = Person("Elizaveta Tilman", "USA", date(2000, 1, 1))

print(f'Age of the person 1: {person_1.get_age()}\nName: {person_1.name}\nCountry: {person_1.country}\nDate of Birth: {person_1.date_of_birth}\n')
print(f'Age of the person 2: {person_2.get_age()}\nName: {person_2.name}\nCountry: {person_2.country}\nDate of Birth: {person_2.date_of_birth}\n')
print(f'Age of the person 3: {person_3.get_age()}\nName: {person_3.name}\nCountry: {person_3.country}\nDate of Birth: {person_3.date_of_birth}')


# Exercise_3

class Calculator():
    def __init__(self, num_1, num_2, operation):
        self.num_1 = num_1
        self.num_2 = num_2
        self.operation = operation

    def calculate(self):
        if self.operation == 'addition':
            return self.num_1 + self.num_2
        if self.operation == 'subtraction':
            return self.num_1 - self.num_2
        if self.operation == 'multiplication':
            return self.num_1 * self.num_2
        if self.operation == 'division':
            return self.num_1 / self.num_2

operation_list = ['addition', 'subtraction', 'multiplication', 'division']
for i in range(len(operation_list)):
    random_num_1, random_num_2 = random.randint(1, 100), random.randint(1, 100)
    print(f'{random_num_1} and {random_num_2}')
    for j in operation_list:
        start_calculation = Calculator(random_num_1, random_num_2, j)
        print(f'{j}: {round(start_calculation.calculate(), 1)}')
    print('')


# Exercise_4

class figure_calculation:
    def __init__(self, figure, side_size):
        self.figure = figure
        self.side_size = side_size

    def circle(self):
        if self.figure == 'circle':
            return [
                round(math.pi * self.side_size ** 2, 2),
                round(2 * math.pi * self.side_size, 2)
            ]

    def triangle(self):
        if self.figure == 'triangle':
            return [
                round((math.sqrt(3) / 4) * side_size ** 2),
                round(3 * side_size)
            ]

    def square(self):
        if self.figure == 'square':
            return [
                round(self.side_size ** 2, 2),
                round(self.side_size * 4, 2)
            ]


figure = ['circle', 'triangle', 'square']
for i in figure:
    side_size = random.randint(1, 100)
    start_calc = figure_calculation(i, side_size)
    print(f'{i.title()}, {side_size}\nArea: {getattr(start_calc, i)()[0]}\nPerimeter: {getattr(start_calc, i)()[1]}\n')

# Exercise_5

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

bst = BinarySearchTree()

for i in range(10):
    bst.insert(i)

print("Searching for elements:")
print(bst.search(4))
print(bst.search(9))


# Exercise_6

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Cannot pop from an empty stack."

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Empty stack."


stack = Stack()
for i in range(1, 101):
    stack.push(i)

print("Stack size:", stack.size())
print("Top element:", stack.peek())
print("\nPopped item:", stack.pop())
print("\nStack size:", stack.size())
print("Top element:", stack.peek())

stack1 = Stack()
print("\nStack size:", stack1.size())
popped_item = stack1.pop()
print("\nPopped item:", popped_item)


# Exercise_7

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, data):
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if current:
            prev.next = current.next


linked_list = LinkedList()


linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(4)

print("Initial Linked List:")
linked_list.display()

linked_list.insert(5)
print("After inserting a new node (5):")
linked_list.display()

linked_list.delete(2)
print("After deleting an existing node (2):")
linked_list.display()


# Exercise_8

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item_name, qty, price):
        item = (item_name, qty, price)
        self.items.append(item)

    def remove_item(self, item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break

    def calculate_total(self):
        total = 0
        sum = 0
        for item in self.items:
            total += item[1]
            sum += item[2]
        return total, sum


cart = ShoppingCart()
item_for_adding = [["Pen blue", 1, 0.7], ["Copybook", 2, 2.3], ["Pen red", 1, 1.1], ["Pen black", 3, 1.9], ["Notebook", 1, 3]]
for i in item_for_adding:
    cart.add_item(i[0], i[1], i[2])

print("Cart:")
for item in cart.items:
    print(item[0], "-", item[1], 'pcs |', "price -", item[2], '$ |', 'sum -', round(item[2] * item[1], 1), '$')

total_qty = cart.calculate_total()
print("Total qty:", total_qty[0], '| final sum:', total_qty[1], '$')

cart.remove_item("Pen red")
print("\nCart updated:")
for item in cart.items:
    print(item[0], "-", item[1], 'pcs |', "price -", item[2], '$ |', 'sum -', round(item[2] * item[1], 1), '$')

total_qty = cart.calculate_total()
print("Total qty:", total_qty[0], '| final sum:', total_qty[1], '$')


# Exercise_9

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Cannot pop from an empty stack.")

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        return self.items


stack = Stack()
for i in range(10, 100, 10):
    stack.push(i)

print("Items:", stack.display())
print("Popped item:", stack.pop())
print("Popped item:", stack.pop())
print("Items:", stack.display())


# Exercise_10

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Cannot dequeue from an empty queue.")

    def is_empty(self):
        return len(self.items) == 0


queue = Queue()
for i in range(10, 100, 10):
    queue.enqueue(i)

print("Current Queue:", queue.items)
print("Dequeued item:", queue.dequeue())
print("Dequeued item:", queue.dequeue())
print("Updated Queue:", queue.items)

# Exercise_11

class Bank:
    def __init__(self):
        self.customers = {}

    def create_account(self, account_number, initial_balance=0):
        if account_number in self.customers:
            print("Account number already exists.")
        else:
            self.customers[account_number] = initial_balance
            print("Account created successfully.")

    def make_deposit(self, account_number, amount):
        if account_number in self.customers:
            self.customers[account_number] += amount
            print("Deposit successful.")
        else:
            print("Account number does not exist.")

    def make_withdrawal(self, account_number, amount):
        if account_number in self.customers:
            if self.customers[account_number] >= amount:
                self.customers[account_number] -= amount
                print("Withdrawal successful.")
            else:
                print("Insufficient funds.")
        else:
            print("Account number does not exist.")

    def check_balance(self, account_number):
        if account_number in self.customers:
            balance = self.customers[account_number]
            print(f"Account balance: {balance}")
        else:
            print("Account number does not exist.")


bank = Bank()
account_1 = ["SB-123", 1000]
print("New a/c No.: ", account_1[0], "Deposit Amount:", account_1[1])
bank.create_account(account_1[0], account_1[1])

account_2 = ["SB-124", 1500]
print("New a/c No.: ", account_2[0], "Deposit Amount:", account_2[1])
bank.create_account(account_2[0], account_2[1])

deposit_sum_1 = 600
print("\nDeposit Rs.", deposit_sum_1,"to A/c No.", account_1[0])
bank.make_deposit(account_1[0], deposit_sum_1)

withdrawal_1 = 350
print("Withdraw Rs.", withdrawal_1, "From A/c No.", account_1[0])
bank.make_withdrawal(account_2[0], withdrawal_1)

print("A/c. No.", account_1[0])
bank.check_balance(account_1[0])

print("A/c. No.", account_2[0])
bank.check_balance(account_2[0])

withdrawal_2 = 1200
print("Withdraw Rs.",withdrawal_1,"From A/c No.",account_2[0])
bank.make_withdrawal(account_2[0], withdrawal_1)

account_3 = ["SB-134", 1500]
print("A/c. No.",account_3[0])
bank.check_balance(account_3[0])

