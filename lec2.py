# Multiple input from user
print('output of Multiple input from user:')
a, b = map(int, input('Enter Two numbers: ').split())
print(f'Output: {a} {b}')
print(f'sum: {a + b}')
print('\n')


# Conditional statement
print('output of Conditional Statement:')
a, b = map(int, input('Enter Two numbers: ').split())
if a > b:
    print(f'{a} is greater than {b}')
elif a < b:
    print(f'{a} is less than {b}')
else:
    print(f'{a} is equal to {b}')

print('\n')


# while loop
a = int(input('Enter a number: '))

print(f'numbers from 1 to {a} are: ')
x = 1
while x <= a:
    print(x, end=' ')
    x += 1
print('\n')


# break in while loop
print('output of break inside loop:')
friends = ["Jarif", "Rafi", "Protik", "Shakib", "Nourin", "Rakib", "Karim"]
for x in friends:
    print(x, end=' ')
    if x == "Nourin":
        break
print('\n')



# Continue in loop
friends = ["Protik", "Rafi", "Omi", "Sadat", "Sajin"]
for x in friends:
    if x == "Omi":
        continue
    print(x, end=' ')

print('\n')



# Range Function
print('output of Range Function:')
q = 0
print('Numbers from 1 to 10')
for x in range(10):
    q += x
    print(x, end=' ')
print('Sum:', q)
print('\n')


# Loop from 20 to 49
print('Numbers from 20 to 50')
for x in range(20, 50):
    q += x
    print(x, end=' ')
print('Sum:', q)

print('\n')

# Loop from 20 to 50 with step 2 (even numbers)
print('Even Numbers from 20 to 50')
for x in range(20, 50, 2):
    q += x
    print(x, end=' ')
print('Sum:', q)

print('\n')

# Loop from 100 to 50 with step -2
print('Numbers from 100 to 50')
for x in range(100, 50, -2):
    q += x
    print(x, end=' ')
print('Sum:', q)

print('\n')


# Assign a string to a variable and print it
name = "Independent 2.0"
print(name)

print('\n')

# Print multiple variables
age = 18
salary = 20000
name = "Mr X"
print(age)
print(salary)
print(name)

print('\n')


# Input from user and print it
ID = input("Enter your ID: ")
print(ID)

print('\n')


# Basic arithmetic operations
a = 50
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a % b)
print(a ** b)

print('\n')


# Boolean operations
m = True
n = False
print(m and n)
print(m or n)
print(not m)

print('\n')

# Assignment operations
a = 10
b = a
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b <<= a
print(b)

print('\n')

# if-else
i = 33
if i < 48:
    print("i is smaller than 15")
    print("inside if block")
else:
    print("i is greater than 15")
    print("inside else block")
print("i'm not at if block & else block")
print('\n')

# elif example
i = 20
if i == 10:
    print("i is 10")
elif i == 15:
    print("i is 15")
elif i == 20:
    print("i is 20")
else:
    print("i ekhane nai")

print('\n')

# for loop with range
for i in range(0, 40, 2):
    print(i)

print('\n')

# while loop with counter
count = 0
while count < 5:
    count += 1
    print("Hello 63_N")

print('\n')

# Function to check even or odd
def evenOdd(x):
    if x % 2 == 0:
        print("even")
    else:
        print("odd")

evenOdd(2)
evenOdd(3)
