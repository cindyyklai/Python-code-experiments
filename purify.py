# Define a function called purify that takes in a list of numbers, removes all odd numbers in the list, and returns the result.
# For example, purify([1,2,3]) should return [2].
def purify(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

print purify([3,1,2,3,5])