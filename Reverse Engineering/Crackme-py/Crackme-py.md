# Crackme-py
- Category : Reverse Engineering
- Points 30

### Description

[crackme.py](https://mercury.picoctf.net/static/f440bf2510a28914afae2947749f2db0/crackme.py)


### Downloads
[crackme.py](./crackme.py)


### Hints

None


## Overview

Anther challenge with nothing to help us - although it turns out to be ridiculously easy.


## Steps

1. Okay... slet's grab the supplied file with wget

   ```
   wget https://mercury.picoctf.net/static/f440bf2510a28914afae2947749f2db0/crackme.py
   ```


2. We open the file in a text editor and see this at the head...

   ```
   01: # Hiding this really important number in an obscure piece of code is brilliant!
   02: # AND it's encrypted!
   03: # We want our biggest client to know his information is safe with us.
   04: bezos_cc_secret = "A:4@r%uL`M-^M0c0AbcM-MFE0g4dd`_cgN"
   05:
   06: # Reference alphabet
   07: alphabet = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
   08:              "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
   09:
   10:
   11:
   12: def decode_secret(secret):
   13:   """ROT47 decode
   14:
   15:   NOTE: encode and decode are the same operation in the ROT cipher family.
   16:   """
   ```

   Which seems to tell us all we need to know!

   a) That the flag is encoded using the ROT47 cipher and stored into the *bezos_cc_secret** variable.
   b) It looks like the encoding uses a bespoke alphabet (line 07 & 08) but a quick check of the [ASCII table](https://www.asciitable.com) shows that it is not special at all


3. So let's just use [CyberChef](https://gchq.github.io/CyberChef/#recipe=ROT47(47)&input=QTo0QHIldUxgTS1eTTBjMEFiY00tTUZFMGc0ZGRgX2NnTg) to do the heavy lifting for us

   And we get the challenge flag straight away

   picoCTF{1|\/|_4_p34|\|ut_******}

5. Cut and paste the displayed flag, and adding the closing brace into the picoCTF window to gain the credit



### Side Notes

1. We could have written a script to do the work for us; reusing the encode function.... but why, when CyberChef can do the work straight off the bat.
