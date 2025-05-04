import stdio
import random
import sys
import math
import stdarray

encoding_parameter = 0
binary_parameter = format(encoding_parameter, '05b')

GUI_mode = None
if binary_parameter[0] == "1":
    GUI_mode = True
elif binary_parameter[0] == "0":
    GUI_mode = False

print(binary_parameter)
print(GUI_mode)
exit()

b = 0
if b%3 == 0:
    print("wtf")

bit_count = format(123456, '08b')
print(bit_count)

a = 18
binary = format(1, '05b')
print(binary)
mask_pattern = binary[2:]
print(mask_pattern)

print(binary[0])

GUI_mode = None
if binary[0] == "1":
    GUI_mode = True
elif binary[0] == "0":
    GUI_mode = False
print(GUI_mode)

if mask_pattern == "001":
    print("string")