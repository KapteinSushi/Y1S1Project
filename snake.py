import sys
import math
import stdio
import stdarray

string = "Hello"
#string = sys.stdin.read()
encoding_parameter = 18
string_length = len(string)

binary_string = "0100"
#temp_parameter = encoding_parameter


def ascii_to_binary(d):
    
    v = 1
    answer = ""
    

    while v <= d // 2:
        v *= 2

    '''Eject out powers of 2 in desending order'''
    while v > 0:
        if d < v:
            #stdio.write(0)
            answer = answer + str(0)
        else:
            #stdio.write(1)
            answer = answer + str(1)
            d -= v
        v //= 2
    print(answer)
    return answer

encoding_parameter_string = ascii_to_binary(number_value=encoding_parameter)
binary_string += ascii_to_binary()
mask_pattern = binary_string[-3:]

'''Function to turn each char into binary'''
def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

'''Call the text_to_binary function to convert the inputted string'''
binary = text_to_binary(string)
print(binary)



def masking_xor(x, y):
        # Hand-in 2 masking function
        if mask_pattern == "000":
            #print("1 == 0 ; no masking")
            return False
        elif mask_pattern == "001":
            #print("y%2 == 0")
            if y%2 == "0":
                return True
            else:
                return False
        elif mask_pattern == "010":
            #print("x%3 == 0")
            if x%3 == "0":
                return True
            else:
                return False


# To ASCII to binary
for i in string:
    print(i)
    ascii_value = ord(i)
    stdio.write(ascii_value + ", ")
