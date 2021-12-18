# Mind Your Ps and Qs
- Category : Cryptography
- Points 20

### Description

In RSA, a small e value can be problematic, but what about N? Can you decrypt this? [values]()https://mercury.picoctf.net/static/3cfeb09681369c26e3f19d886bc1e5d9/values

### Downloads
[values](./values)

### Hints

1. Bits are expensive, I used only a little bit over 100 to save money

## Overview

We need to crack RSA encryption. In theory, this shouldn't be possible without a lot of compute resource, so there has to be a weakness in the keys used to encrypt the data.


## Steps

1. Let's get the supplied file

   ```
   wget https://mercury.picoctf.net/static/3cfeb09681369c26e3f19d886bc1e5d9/values
   ```

  And look at the Content

  ```
  > cat values
  Decrypt my super sick RSA:
  c: 8533139361076999596208540806559574687666062896040360148742851107661304651861689
  n: 769457290801263793712740792519696786147248001937382943813345728685422050738403253
  e: 65537
  ```

  Ok, we've the cipher-text (c), and the public-key (n & e) - just need to figure out how to proceed.


2. A search on Google for "RSA attack tool" found many tools that could do the heavy lifting without us having to lift a finger ...

```
./RsaCtfTool/RsaCtfTool.py -n 769457290801263793712740792519696786147248001937382943813345728685422050738403253 -e 65537 --uncipher 8533139361076999596208540806559574687666062896040360148742851107661304651861689
```

  After some processing output, we get our key

  ```
  picoCTF{sma11_N_n0_g0od_******}
  ```

3. So we just need to cut and paste the displayed flag into the picoCTF window to gain the credit








### Side Notes

1. We should be able to roll-our-own factorisation using GMPY2 to handle the large numbers involved ... and crack the code that way.
