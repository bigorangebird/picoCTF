import string

message = []

#
# Read in the encrypted string
#
with open("message.txt") as file:
    for line in file: 
        message = line.strip().split(" ") #or some other preprocessing


#
# Create out mapping list
#
cypherArray = list(string.ascii_lowercase)
cypherArray.extend(list(string.digits))
cypherArray.append('_')

decMessage = ""

#
# For each character in the encrypted message
#
for character in message:
    # Translate the imported text to an integer
    encChar = int(character)

    # Find the mod37 of that number
    charMod = encChar % 37

    # Look up the mod37 value in the cypher list
    decChar = cypherArray[charMod]

    # Add the looked-up character to our decryption string
    decMessage += decChar


# Display the decrypted string
print(decMessage)