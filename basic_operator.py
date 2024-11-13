# Basic operator 
'''
print("Number 1 = ")
number_1 = int(input())
print("Number 2 = ")
number_2 = int(input())

# Sum 
sum = number_1 + number_2

# Minus 
minus = number_1 - number_2

# Multiply
multiply = number_1 * number_2

# Division 
division = number_1 / number_2

# Power 
power = number_1 ** number_2


print("Sum = ", sum)
print("Minus = ", minus)
print("Multiply = ", multiply)
print("Division = ", division)
print("Power = ", power)


# Compare Operator
print("Number_1 > Number_2", number_1 > number_2)
print("Number_1 < Number_2", number_1 < number_2)
print("Number_1 >= Number_2", number_1 >= number_2)
print("Number_1 <= Number_2", number_1 <= number_2)
print("Number_1 != Number_2", number_1 != number_2)
print("Number_1 == Number_2", number_1 == number_2)


# Assignment Operator
print("Number 4 = ")
number_4 = int(input()) # For example: number_4 = 2
print("Total = ")
Total = int(input()) # For example: Total = 1

Total += number_4
print("Total = " + str(Total)) # 3
Total -= number_4
print("Total = " + str(Total)) # 1
Total *= number_4
print("Total = " + str(Total)) # 2
Total /= number_4
print("Total = " + str(Total)) # 1


# in and not in
print("Type any word: ")
word = input()
print('H' in word)

'''

# is and is not
print("Number 5 = ")
number_5 = int(input())
print("Number 6 = ")
number_6 = int(input())
print("Number 5 equal Number 6:", number_5 is number_6)
print("Number 5 not equal Number 6:", number_5 is not number_6)