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


# Sort elements in array (Descending order)
array_list_sort_descending = []
number_n = int(input("The number of elements in array are: "))

for v in range(0, number_n):
    x = int(input("Type the numbers into array: "))
    array_list_sort_descending.append(x)

for i in range(len(array_list_sort_descending)):
    for j in range(len(array_list_sort_descending) - i - 1):
        if (array_list_sort_descending[j] < array_list_sort_descending[j + 1]):
            temp = array_list_sort_descending[j]
            array_list_sort_descending[j] = array_list_sort_descending[j + 1]
            array_list_sort_descending[j + 1] = temp
            

print(array_list_sort_descending)
   
# Sort elements in array (Ascending order)
array_list_sort_ascending = []
number_n = int(input("The number of elements in array are: "))

for v in range(0, number_n):
    x = int(input("Type the numbers into array: "))
    array_list_sort_ascending.append(x)

for i in range(len(array_list_sort_ascending)):
    for j in range(len(array_list_sort_ascending) - i - 1):
        if (array_list_sort_ascending[j] > array_list_sort_ascending[j + 1]):
            temp = array_list_sort_ascending[j]
            array_list_sort_ascending[j] = array_list_sort_ascending[j + 1]
            array_list_sort_ascending[j + 1] = temp
            

print(array_list_sort_ascending)
'''

# a list containing all the odd elements of list lst on the screen
lst = []
n = int(input("Nhap so phan tu: "))

for i in range(0, n):
    lst.append(int(input("Nhap cac phan tu: ")))

answer = []
for j in range(len(lst) + 1):
    if j % 2 != 0:
        answer.append(j)

print(answer)