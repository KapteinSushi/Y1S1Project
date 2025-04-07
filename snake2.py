import sys
import stdio
import stdarray

string = "Hi"
#string = stdio.readAll()
encoding_parameter = 18
string_length = len(string)
binary_string = "0100"

# Function to turn each char into ascii then to binary
def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

#Call the text_to_binary function to convert the inputted string
binary_string += text_to_binary(string)
binary_string += "0000"
print(binary_string)