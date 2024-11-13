# An integer n from the user and displays the sum of numbers from 1 to n on the screen
## For loop 
'''
print("Type n from keyboard: ")
n = int(input())
total_for = 0
for i in range(1, n + 1): # range(1, 5): 1 to 4
    total_for += i
    print(total_for)

print(total_for)

## While loop
print("Type m from keyboard: ")
m = int(input())
total_while = 0
j = 0

while j <= m:
    total_while += j
    j = j + 1
    print(j)
    print(total_while)

print(total_while)


# Two integers a and b from the user and displays the sum of odd numbers between a and b on the terminal
## For loop
print("Type a = ")
a = int(input())
print("Type b = ")
b = int(input())
total_2 = 0
if a < b:
    for i in range(a , b + 1):
        if i % 2 != 0:
            total_2 += i
    print(total_2)


## While loop
total_3 = 0
while a <= b:
    if a % 2 != 0:
        print(a)
        total_3 += a
    a = a + 1
print(total_3)


# Takes a string s from the keyboard and displays characters which are not 'y' in string s on the terminal
## First way
print("Type any string: ")
s = input()
for i in s:
    if i != 'y':
        print("Current character normal way: ", i)

## Second way: use 'continue'
for i in s:
    if i == 'y':
        continue
    print("Current character use 'continue':", i)
'''

# Takes an integer a from user and displays products of a and numbers from 1 to 7 on the terminal.
a = int(input())
j = 1
total = 1
while j <= 7:
    total = a * j
    print(a, "*", j, "=", total)
    j = j + 1
    
    #print(j)