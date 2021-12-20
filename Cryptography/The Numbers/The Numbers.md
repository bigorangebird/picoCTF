# The Numbers
- Category : Cryptography
- Points 50

### Description

The [numbers](https://jupiter.challenges.picoctf.org/static/f209a32253affb6f547a585649ba4fda/the_numbers.png)... what do they mean?

### Downloads
[numbers](./the_numbers.png)

### Hints

1. The flag is in the format PICOCTF{}


## Overview

We need to figure out a way to crack a one-time pad using a weakness in the encoding.


## Steps

1. As always, let's start by getting the supplied file

   ```
   wget https://jupiter.challenges.picoctf.org/static/f209a32253affb6f547a585649ba4fda/the_numbers.png
   ```

  And open it in an editor to take a look at what we've got.


2. Looks very much like these numbers are the flag .... seven characters before an opening brace, followed by a series of characters, and a closing brace to finish.

   The third and fifth encoded characters are both 3 ... and we're looking for a flag in the format of *picoCTF{...}*

   So both the third and fifth characters would be three.

   So it seems like a simple substitution cipher - the each character (ignoring case) represented by it's index in the alphabet


      a|A = 1
      b|B = 2
      c|C = 3
      .
      .
      x|X = 24
      y|Y = 25
      z|Z = 26


3. There may well be an automated way to do this - but it seems just as quick to do it by hand

   The result being

    picoctf{thenumbers*****}


6. Once again, not quite the format we are expecting (neither wrapped with *picCTF{...}* nor is it word-like. But we'll submit it anyway

   Which worked fine - so we gain the credit








### Side Notes

None
