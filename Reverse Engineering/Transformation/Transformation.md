# Transformation
- Category : Reverse Engineering
- Points 20

### Description

I wonder what this really is... [enc](https://mercury.picoctf.net/static/dd6004f51362ff76f98cb8c699510f23/enc) ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

### Downloads
[enc](./enc)

### Hints

1. You may find some decoders online


## Overview

This task is more about reading between the lines of the hints....

## Steps

1. First, let's grab the supplied file with wget

```
wget https://mercury.picoctf.net/static/dd6004f51362ff76f98cb8c699510f23/enc
```


2. Running the *file* command against the *enc* file suggest that this is just text
```
file enc
enc: Unicode text, UTF-8 text, with no line terminators
```

3. Using the *cat* command against the file shows from chinese characters
```
cat enc
灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰摤捤㤷慽
```

4. Using the CyberChef 'magic' recipe, the flag can be decoded without needing to use any of the code included in the Description. The 'Magic' recipe identified *UTF-16BE* encoding.
```
picoCTF{16_bits_inst34d_of_8_******}
```

5. Cut and paste the displayed flag into the picoCTF window to gain the credit

------------------------------

An alternative approach would be to write a [Python script](./decode.py), using the code in the description as a hint as to how the encryption occurred.






### Side Notes

1. Seems very odd that both of the helpful hints to this 15 point challenge take you to more advanced challenges!
