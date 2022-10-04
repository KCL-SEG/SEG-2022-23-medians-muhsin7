"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
def median(sorted):
    sorted.sort()
    length = len(sorted)
    if (length % 2 == 0):
        return (sorted[length//2]+sorted[(length//2)+1])/2
    else:
        return sorted[length//2]

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)

print("median: " + str(median(numbers)))
