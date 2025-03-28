import stdio

# encoding_parameter
align_square_size = 0
if align_square_size not in range(0,32):
    stdio.writeln("ERROR")
    

if ((align_square_size - 1)%2 != 0) or (align_square_size < 5):
    stdio.writeln("ERROR: Alignment pattern out of bounds")