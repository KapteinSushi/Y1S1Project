import sys
import stdio
import stdarray

a = "01000100100001101001000011101100000100011110110000010001111011000001000"
print(len(a))

string = "Hi"
#string = stdio.readAll()
encoding_parameter = 18
string_length = len(string)
binary_string = "5100"
print(binary_string[2])
# Function to turn each char into ascii then to binary
def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

#Call the text_to_binary function to convert the inputted string
binary_string += text_to_binary(string)
binary_string += "0000"
print(binary_string)