# List comprehention.
my_list = [i**2 for i in range(1,11)]

my_file = open("output.txt", "r+")

for val in my_list:
    # Write each element of that list to output.txt.
    my_file.write(str(val) + "\n")

my_file.close()

# Read from output.txt.
my_file = open("output.txt", "r")

print my_file.read()

my_file.close()

# Create a file text.txt for writing.
file = open("text.txt", "w")
file.write("I'm the first line of the file!\n")
file.write("I'm the second line.\n")
file.write("Third line here, boss.\n")
file.close()

my_file = open("text.txt", "r")

print my_file.readline()
print my_file.readline()
print my_file.readline()

my_file.close()

# Open a file for writing.
with open("text.txt", "w") as my_file:
    my_file.write("Yes")

# If the file is not closed, close it.
if my_file.closed == False:
    my_file.close()

print my_file.closed