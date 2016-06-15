# Define a function called count that has two arguments called sequence and item.
# Return the number of times the item occurs in the list.
# For example: count([1,2,1,1], 1) should return 3 (because 1 appears 3 times in the list).
def count(sequence, item):
    total = 0;
    for t in sequence:
        if t == item:
            total += 1
    return total

print count([4, 'foo', 5, 'foo'], 5)