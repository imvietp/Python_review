# Returns the smallest number in lst on the screen.

array = []
n = int(input('Enter how many elements you want: '))

for i in range(0, n):
    x = int(input('Enter the numbers into the array: '))
    array.append(x)

min = array[0]

for j in array:
    if j < min:
        min = j
    print(j)

print(min)
