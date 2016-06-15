# Write a function called median that takes a list as an input and returns the median value of the list.
def median(numbers):
    numbers = sorted(numbers)
    length = len(numbers)

    if len(numbers) % 2 == 0:
        mid = length / 2
        first = numbers[mid - 1]
        second = numbers[mid]

        return (first + second) / 2.0
    else:
        return numbers[length / 2]


print median([2, 3, 5, 8])