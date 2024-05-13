# ASCII
# A - American
# S - Standard
# C - Code
# I - Information
# I - Interchange

ascii_code = "A"
print(ord(ascii_code))

ascii_code = 65
print(chr(ascii_code))

#converting all the letters in the below variable to ASCII code
lecture = "GCIS-123"

for letters in lecture:
    print(ord(letters), end = ' ')


print("\n")

#converting all the elements in the below ASCII code to letters
code = [72, 69, 89]

for x in code:
    print(chr(x), end = " ")