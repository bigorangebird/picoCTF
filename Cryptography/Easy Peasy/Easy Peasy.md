# Easy Peasy
- Category : Cryptography
- Points 40

### Description

A one-time pad is unbreakable, but can you manage to recover the flag? (Wrap with picoCTF{}) *nc mercury.picoctf.net 36449* [otp.py](https://mercury.picoctf.net/static/2cebaadd44657a7b22ddff3d0401775f/otp.py)

### Downloads
[otp.py](./otp.py)

### Hints

1. Maybe there's a way to make this a 2x pad

## Overview

We need to figure out a way to crack a one-time pad using a weakness in the encoding.


## Steps

1. As always, let's start by getting the supplied file

   ```
   wget https://mercury.picoctf.net/static/2cebaadd44657a7b22ddff3d0401775f/otp.py
   ```

  And open it in an editor to take a look at what is happening.


2. Now lets take a look at the web service at

   ```
   nc mercury.picoctf.net 36449
   ```

   It tells us what the encrypted challenge flag is.
   Then it prompts the user for some input - encodes it - and displays the encoded text string; repeating the input request/encoding/display forever. Simple enough.


3. Ok, let us look at *otp.py* and see if there are any weaknesses.

   The encoding is based on a 50000 long key-file (which is on the server, so we can't access it)
   The encoding occurs on line 42

   ```
   result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), ui, key))
   ```

   Which simply takes each plaintext character (p), finds it's unicode value (ord()) and XORs (^) it with the next character in the key sequence.

   We can also see that after the program starts and before the user is asked for their first input, that our challenge flag is encrypted (lines 9-22)

   ```
   09: def startup(key_location):
   10: 	flag = open(FLAG_FILE).read()
   11:	kf = open(KEY_FILE, "rb").read()
   12:
   13: 	start = key_location
   14:	stop = key_location + len(flag)
   15:
   16:	key = kf[start:stop]
   17:	key_location = stop
   18:
   19:	result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), flag, key))
   20:	print("This is the encrypted flag!\n{}\n".format("".join(result)))
   21:
   22:	return key_location
   ```

   But the clincher, is on lines 34-36
   ```
   29: start = key_location
   30: stop = key_location + len(ui)
   31:
   32: kf = open(KEY_FILE, "rb").read()
   33:
   34: if stop >= KEY_LEN:
   35:    stop = stop % KEY_LEN
   36:    key = kf[start:] + kf[:stop]
   37: else:
   38:    key = kf[start:stop]
   39: key_location = stop
   ```
   If the program has processed more than KEY_LEN (aka 50000) characters, then
   loop back to the start of the key_file.

   This seems reasonable - otherwise there will be nothing against which to encode
   any further input.

   However, it does mean that this ISN'T a one-time-pad; it is a repeated use pad
   and, therefore, crackable.



4. We know that the encypted flag is 64 characters long. We also know (line 19) that each character encoded results in two hex characters. So the flag is 32 characters long.

  If, at the prompt for input, we enter a string that is 49968 (50000 - 32) characters long; then we are guaranteed to not only cause the key-file to wrap, but we are also guarantee to wrap it back to the start of the keyfile.

  We know that (as pseudo-code)

    PlainTextChar XOR KeyChar = CipherTextChar

  Therefore, if we can force PlainText to be a series of 1's (ie 0xFF) then
  the CipherText output will be the KeyChar (as Hex)

  If we can input thirty-two 0xFF, we can expose the first thirty-two characters of the KEY_FILE
  And, using this, we can XOR the encrypted against those thirty-two characters of the KEY_FILE
  This will give us the flag (in Hex) because

        Char XOR <an unknown> XOR <the same unknown> = Char


5. We could the first part of this via a short python script at the command prompt...

  ```
  > python3 -c "print('\x00'*(50000-32)+'\n'+'\x00'*32)" | nc mercury.picoctf.net 36449
  ```

  Which, focusing one just the important output, would give us the first thirty-two parts of the key file data

  ```
  What data would you like to encrypt? Here ya go!
  622764205c786131695c7830325c7863645c7862615c7863345c786562316e5c
  ```

  So, we can now use CyberChef XOR function to do the processing ... yielding an XOR'd value of

      75302b38697a8717f0faee9c0*********



6. Once again, not the format we are expecting (neither wrapped with *picCTF{...}* nor is it word-like.
   But we'll wrap it in *picoCtF{...}* and submit.

   picCTF{75302b38697a8717f0faee9c0*********}

   Which works fine when we paste it into the picoCTF window; and we gain the credit








### Side Notes

None
