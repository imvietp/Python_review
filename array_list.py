'''
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


# Display the sum of all elements in the list on the screen
array_list = []
m = int(input())

for i in range (0, m):
    y = int(input('Enter the numbers into the array: '))
    array_list.append(y)

sum = 0
for j in array_list:
    sum += j

print(sum)
'''

# Sort elements in array
array_list_sort = []
number_n = int(input("The number of elements in array are: "))

for v in range(0, number_n):
    x = int(input("Type the numbers into array: "))
    array_list_sort.append(x)

for i in range(len(array_list_sort)):
    for j in i:
        if array_list_sort[i] > array_list_sort[j]:
            temp = array_list_sort[i]
            array_list_sort[i] = array_list_sort[j]
            array_list_sort[j] = temp

print(i)            