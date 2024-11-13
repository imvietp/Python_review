# An integer n from the user and displays the sum of numbers from 1 to n on the screen
## For loop
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
