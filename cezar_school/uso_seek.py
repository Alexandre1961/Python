#!/usr/bin/python
from math import pow
num = pow(2,3)
print(num)

# Open a file
fo = open("relatorio.txt", "r+")
print("Name of the file: ", fo.name)

# Assuming file has following 5 lines
# This is 1st line
# This is 2nd line
# This is 3rd line
# This is 4th line
# This is 5th line

#linha 0
line = fo.readline()
print(f"Read Line 0: {line}")
#linha1
line = fo.readline()
print(f"Read Line 1: {line}")
#linha2
line = fo.readline()
print(f"Read Line 2 {line}")

# Again set the pointer to the beginning


fo.seek(0, 1)
line = fo.readline()
print(f"Read Line do posição atual: {line}")

fo.seek(0, 0)
line = fo.readline()
print(f"Read Line do inicio: {line}")

# Close opend file
fo.close()

