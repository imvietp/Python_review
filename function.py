# Calculate sum of element in array
'''
def sum(array):
    total = 0
    for i in array:
        total += i

    return total


lst = [1, 3, 5]
print(sum(lst))
'''

# Print the largest element among 3 elements
def largest_element (a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
    
a = int(input())
b = int(input())
c = int(input())
print(largest_element(a, b, c))