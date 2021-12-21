# New Caesar
- Category : Cryptography
- Points 60

### Description

We found a brand new type of encryption, can you break the secret code? (Wrap with picoCTF{}) mlnklfnknljflfjljnjijjmmjkmljnjhmhjgjnjjjmmkjjmijhmkjhjpmkmkmljkjijnjpmhmjjgjj [new_caesar.py](https://mercury.picoctf.net/static/43182e6d4527ef0916b2ce43883227b7/new_caesar.py)


### Downloads
[new_caesar.py](./new_caesar.py)


### Hints

1. How does the cipher work if the alphabet isn't 26 letters?

2. Even though the letters are split up, the same paradigms still apply


## Overview

We need to figure out a way to crack a one-time pad using a weakness in the encoding.


## Steps

1. As always, let's start by getting the supplied file

   ```
   wget https://mercury.picoctf.net/static/43182e6d4527ef0916b2ce43883227b7/new_caesar.py
   ```

  And open it in an editor to take a look at what is happening.


2. Ok, this stretched my python skills (which were non-existent before I started the picoCTF challenges).. but I think I've got it.

    All it seems to do is to encode the challenge flag - and then output the encoded flag (which we've been given)

    ```
    24: b16 = b16_encode(flag)
    25: enc = ""
    26: for i, c in enumerate(b16):
    27: 	enc += shift(c, key[i % len(key)])
    ```

    But it seems that there are two steps to the process ... calling an *encode function* (line 24) and then a *shift function* against the encoded text (line 27)

    We can also see that (line 21) that they key can only contain characters in the first sixteen chacters of the alphabet (line 04) AND that the length of the *key* is just one character.

    ```
    03: LOWERCASE_OFFSET = ord("a")
    04: ALPHABET = string.ascii_lowercase[:16]

    19: flag = "redacted"
    20: key = "redacted"
    21: assert all([k in ALPHABET for k in key])
    22: assert len(key) == 1
    ```

    Now, because *len(key) == 1*; and because *X mod 1 == 1*; we can rewrite line 27 to be

    ```
    27: 	enc += shift(c, key)
    ```
    Therefore, the second parameter to the shift function is always the same ... the value of *key*



3. To build a decoder, will need to take the encoded text, unshift it and the unencode it.

   The encoder seems quite straight forward, so we will deal with that first.
   ```
   06: def b16_encode(plain):
   07: 	enc = ""
   08: 	for c in plain:
   09:		 binary = "{0:08b}".format(ord(c))
   10:		 enc += ALPHABET[int(binary[:4], 2)]
   11:		 enc += ALPHABET[int(binary[4:], 2)]
   12:	return enc
   ```

   It processes some plaintext (line 6) ... processing each character in turn (line 8).
   For each character, it calculates (using the Python *ord()* function) the unicode value (e.g "a" = 97)
   It then uses the Python *format* function to convert this value into a byte (8 bits).

   The routine the takes the left-most 4 bits of the byte, and uses the decimal value of that value (0..15) as an index to ALPHABET (which contains a-p, the first 16 letters of the alphabet: line 04).
   That character is added to the encoded output.
   The process is repeated for the right-most 4 bits of the byte; with the final value added again to the encoded output.

   This whole process is repeated for every for every character of the plaintext; generating two characters for every one input into the encoding function.

   To reverse the encoding - we simply need to
   a) lookup the index in the ALPHABET array of each encoded character
   b) convert the index value to a 4-bit binary representation (as each value will always be 0...15)
   b) then, for every pair of characters ... join the two values together in sequence to give an 8 bit value. This value will be a unicode value ... which can be converted back to a character.

   ```
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
    ```


4. Now the *shift* function .... and we also need to include some of the *main* as well

   I've used the simplified version for line 27 (as described above)

   ```
   14: def shift(c, k):
   15: 	  t1 = ord(c) - LOWERCASE_OFFSET
   16:  	t2 = ord(k) - LOWERCASE_OFFSET
   17:  	return ALPHABET[(t1 + t2) % len(ALPHABET)]

   26: for i, c in enumerate(b16):
   27:  	enc += shift(c, key[1])
   ```

   So, we start on line 26 .... the python *enumerate* function iterates through the entities (characters) within the *b16* variable (which contains the output from the encoding function); and it generates two value ... the first being a counter (here we use *i* to hold that value) and the second the entity (and we use *c* to hold that value).

   In the original version of line 27, it appeared that the value of *i* was being passed to the *shift* function - but in the simplified version, we can see that whilst the *shift* function is passed two parameters ... the second parameter is always the single character value of the *key* variable. The first parameter is the entity of the loop.


   So - for a 10 character plaintext string, the *b16_encode* function will return 20 characters. The *shift* function will then process each of those 20 characters in turn.

   The *shift* function itself calculates two intermediate variables, *t1* and *t2*

   *t1* calculates the unicode value of the entity and then subtracts from that the unicode value of "a" (line 3). So, if the entity was "a" ... the result would be the unicode value of "a" (97) minus the unicode value of "a" (97) .... 0; if the entity were "d", the result would be 3 (100 - 97 = 3).

   *t2* calculates the unicode value of the *key* character minus the unicode value of "a".

   The function then adds *t1* and *t2* togther ... and finds the modulo 16 (the length of the variable ALPHABET, which is defined on line 4 as being 16). The function then looks up, and returns, character that is at the index of ALPHABET referenced by that final value.


   So, if *c* was "a" .. and let's say that *key* is "a" .... the *t1* will be 0 (being 97 - 97) and *t2* will be 0 (being 97 - 97)

   *t1* + *t2* will be 0 (0 + 0) .... and the modulo 16 of 0 is 0
   The character value of ALPHABET at index 0 is "a"

   So the encode function will return "a"


5. Let's take a closer look and some other values output by the shift function.

    With a *key* value of "a" .... whatever value of *c* is simply reflected back
    With a *key* valud of "b" .... the output value is the "next" value in the ALPHABET array after the input value (looping back to the start of the array if we reach the end)
    With a *key* value of "c" ... the output value is the "second next" value in the array

   It would seem that the output value is always going to be the *nth* value of the array after the input value, where *n* is the index of the value of the *key*


   So, to unshift .... we can just return *ALPHABET[n]* where n is the value of ALPHABET at index (the index in ALPHABET of *c* plus the index in ALPHABET of *k*) modulo 16.

   Which is the same as simply adding the offset rather than subtracting the offset when calculating *t1* and *t2*

   ```
   def unshift(c,k):
       # Simply invert the initial translation has the same effect
   	t1 = ord(c) + LOWERCASE_OFFSET
   	t2 = ord(k) + LOWERCASE_OFFSET
   	return ALPHABET[(t1 + t2) % len(ALPHABET)]
  ```


6. We still need to know the value *key* of key before this will work.... but there are only 16 possibilities, so we can brute-force it.

  ```
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
  ```

  Only two values (keys : f & g) are reported as being isprintable

  ```
a False ùÙùßÑÜÝÞÑÛ
                  ÚÑÝÐÝ
                       ÛÛÓÞÜÑÓ
ÚÝ
b False /
/ ê
àâíîïâìëâîáîììäïíâäëî
c False !01ûñóþÿð!óý-üóÿò ÿ.ý ýõ  !ðþóõ-/üÿ
d False 2A,AB
1?1112>0     ,32>
e False CR=RS=DCOB@BBBCOA
f True TcNcd.N$&!"U#T& P/&"%S"Q S (SST#!&(PR/"
g True et_tu?_5723f4e71a0736d3b1d19dde4279ac03
h False v`@`FHCDwEvHBrAHDGuDsBuBJuuvECHJrtAD
i False qQqWYTUVYSRYUXUSS[VTY[RU
j False §§¨bhjefgjdcjfifddlgejlcf
k False ©¸¸¹sy{vwªx©{u¥t{wz¨w¦u¨u}¨¨©xv{}¥§tw
l False ºÉ¤ÉÊ¤»º¶¹·¹¹¹º¶¸
m False ËÚµÚÛµÌËÇÊÈÊÊÊËÇÉ
n False ÜëÆëì¦Æ¬®©ªÝ«Ü®¨Ø§®ª­ÛªÙ¨Û¨ ÛÛÜ«©® ØÚ§ª
o True íü×üý·×½¿º»î¼í¿¹é¸¿»¾ì»ê¹ì¹±ììí¼º¿±éë¸»
ÈèÎÀËÌÿÍþÀÊúÉÀÌÏýÌûÊýÊÂýýþÍËÀÂúüÉÌ

  ```

  Of the two, key "g" seems more likely to be correct.


6. We'll wrap the plaintext for key "g" in *picoCtF{...}* and submit to see if that works.

   picCTF{et_tu?_5723f4e71a0736d3b1d19dde4279ac03}

   Which works; so we gain the credit








### Side Notes

None
