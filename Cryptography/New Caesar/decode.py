import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

CIPHERTEXT = "mlnklfnknljflfjljnjijjmmjkmljnjhmhjgjnjjjmmkjjmijhmkjhjpmkmkmljkjijnjpmhmjjgjj"


def b16_decode(ciphertext):
    decodedText = ""
    for x in range(0, len(ciphertext), 2):
        # lookup the index in the ALPHABET array of each encoded character
        # which is the same as the unicode value minus 97
        ct1 = ord(ciphertext[x]) - 97
        ct2 = ord(ciphertext[(x+1)]) - 97

        # convert the index value to a 4-bit binary representation (as each value will always be 0...15)
        b_ct1 = "{0:04b}".format(ct1)
        b_ct2 = "{0:04b}".format(ct2)

        # then, for every pair of characters ... join the two values together in sequence to give an 8 bit value.
        b_ct = b_ct1 + b_ct2

        # converted back to a character.
        decodedText += chr(int(b_ct,2))

    return decodedText


def unshift(c,k):
    # Simply invert the initial translation has the same effect
	t1 = ord(c) + LOWERCASE_OFFSET
	t2 = ord(k) + LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]


# Iterate through the possible keys
for key in ALPHABET:

    unshiftedText = ""
    for i, c in enumerate(CIPHERTEXT):
        # Unshift the cipher text based on the assumed key for this iteration
    	unshiftedText += unshift(c, key)

    # Then unshift the decoded unshifted text
    plaintext = b16_decode(unshiftedText)

    # We can then use the Python function *isprintable* to help us check
    # whether the result of the decoding looks 'reasonable' or not
    
    print(key, plaintext.isprintable(), plaintext)
