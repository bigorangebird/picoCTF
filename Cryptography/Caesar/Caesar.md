# New Caesar
- Category : Cryptography
- Points 60

### Description

Decrypt this [message](https://jupiter.challenges.picoctf.org/static/7d707a443e95054dc4cf30b1d9522ef0/ciphertext).


### Downloads
[message](./ciphertext)


### Hints

1. caesar cipher [tutorial](https://learncryptography.com/classical-encryption/caesar-cipher)


## Overview

Straightforward caesar cipher to decode


## Steps

1. As always, let's start by getting the supplied file

   ```
   wget https://jupiter.challenges.picoctf.org/static/7d707a443e95054dc4cf30b1d9522ef0/ciphertext
   ```

  And open it in an editor to take a look at what is happening.

  ```
  picoCTF{gvswwmrkxlivyfmgsrhnrisegl}
  ```


2. Ok, so we just need to load the main part of the challenge flag into CyberChef and play with different settings for the ROT cipher to see if we can get some useful plaintext.

  Yes - rotation of 22 works

  ```
  crossingtherubicond******
  ```



6. We'll wrap the plaintext back in *picoCtF{...}* and submit to gain the credit.

   picCTF{crossingtherubicond******}









### Side Notes

None
