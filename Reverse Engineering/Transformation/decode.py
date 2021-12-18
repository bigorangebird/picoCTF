# The encoding routine
# ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
#
# Took the first character, converted to the unicode (ord()) bit shifted left 8 bits (<<8)
# Then took the unicode value of the second character
# Then added the two values together before converting the total back as a character (chr())
# Store this character in the output string
# .. then move to the next pair of characters
#

# File containing the encrypted text
filename  = "enc"

# Open the file (read-mode)
with open (filename, "r") as myfile:
    # Read the contents
    ciphertext=myfile.read()


# string to output to
outputString = ""

# loop through each character of the ciphertext
for x in ciphertext:
    # Extract the first character by
    # - obtaining the unicode for the character (ord())
    # - bitmasking away the second half of the value (&FF00)
    # - bitshift to the right by 8 bits (>>8)
    # - re-encoding the resultant value as a character (chr())
    # - Add the character to the output string
    outputString += chr((ord(x)&0xFF00)>>8)
    # Extract the second character by
    # - obtaining the unicode for the character (ord())
    # - bitmasking away the first half of the value (&00FF)
    # - re-encoding the resultant value as a character (chr())
    # - Add the character to the output string
    outputString += chr(ord(x)&0xFF)

# print string
print(outputString)
