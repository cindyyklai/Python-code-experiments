# The string in the editor is garbled in two ways:

# First, our message is backwards;
# Second, the letter we want is every other letter.
# Use list slicing to extract the message and save it to a variable called message.

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"

length = len(garbled)
message = garbled[::-2]