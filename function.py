# Calculate sum of element in array

def sum(array):
    total = 0
    for i in array:
        total += i

    return total


lst = [1, 3, 5]
print(sum(lst))