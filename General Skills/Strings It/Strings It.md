# Strings It
- Category : General Skills
- Points 100

### Description

Can you find the flag in [file](https://jupiter.challenges.picoctf.org/static/fae9ac5267cd6e44124e559b901df177/strings) without running it?

### Downloads
[file](./strings)


### Hints

1. [strings](https://linux.die.net/man/1/strings)


## Overview

2+2 seems difficult in comparison


## Steps

1. Use *wget* to grab the file

   ```
   wget https://jupiter.challenges.picoctf.org/static/fae9ac5267cd6e44124e559b901df177/strings
   ```

2. Use the *strings* command to see if there is a challenge flag embedded in the file ... just a possibility :-)

   ```
   > strings strings | grep pico
   picoCTF{5tRIng5_1T_******}
   ```

2. Submit the flag into the picoCTF window to gain the credit



### Side Notes

None
