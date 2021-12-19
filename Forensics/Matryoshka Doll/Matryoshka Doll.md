# Matryoshka Doll
- Category : Forensics
- Points 30

### Description

Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: [this](https://mercury.picoctf.net/static/f6cc2560a70b1ea811c151accba5390f/dolls.jpg)

### Downloads
[dolls.jpg](./dolls.jpg)

### Hints

1. Wait, you can hide files inside files? But how do you find them?

2. Make sure to submit the flag as picoCTF{XXXXX}



## Overview

Like the dolls, this challenge is about extracting files hidden within files.


## Steps

1. From the command line, run the *wget* command to download the file

   ```
   https://mercury.picoctf.net/static/f6cc2560a70b1ea811c151accba5390f/dolls.jpg
   ```

2. Trying the obvious, I used the *unzip -l* (look) option on the file

   ```
   > unzip -l dolls.jpg
   Archive:  dolls.jpg
   warning [dolls.jpg]:  272492 extra bytes at beginning or within zipfile
     (attempting to process anyway)
     Length      Date    Time    Name
   ---------  ---------- -----   ----
      383936  03-16-2021 00:23   base_images/2_c.jpg
   ---------                     -------
      383936                     1 file
   ```

   The warning message about extra bytes tells us that there is something a little strange going on.

3. Proceeding to unzip

   ```
   > unzip dolls.jpg
   Archive:  dolls.jpg
   warning [dolls.jpg]:  272492 extra bytes at beginning or within zipfile
     (attempting to process anyway)
   replace base_images/2_c.jpg? [y]es, [n]o, [A]ll, [N]one, [r]ename: y
     inflating: base_images/2_c.jpg  
   ```

4. We see that a sub-directory *base_images* has been created, and in it another file (2_c.jpg).
   Let's traverse to the sub-directory and attempt the unzip again until we can go no further

   ```
   > cd base_images
   > unzip 2_c.jpg
   Archive:  2_c.jpg
   warning [2_c.jpg]:  187707 extra bytes at beginning or within zipfile
     (attempting to process anyway)
     inflating: base_images/3_c.jpg  

   > cd base_images/
   > unzip 3_c.jpg
   Archive:  3_c.jpg
   warning [3_c.jpg]:  123606 extra bytes at beginning or within zipfile
     (attempting to process anyway)
     inflating: base_images/4_c.jpg

   > cd base_images
   unzip 4_c.jpg
   Archive:  4_c.jpg
   warning [4_c.jpg]:  79578 extra bytes at beginning or within zipfile
     (attempting to process anyway)
     inflating: flag.txt    
   ```


5. After four levels, we now seem to have a flag file. So let's take a peek

   ```
   > cat flag.txt
   picoCTF{ac0072c423ee13bfc0b166af7*******}
   ```

   Hmmm, the flag looks a little odd. It is wrapped with *picoCTF{...}* but previous challenges have yeilded a word-like message. As this message only uses the characters 0-9 and a-f, this might well be hex format and need further decoding

6. Loaded the code into CyberChef, but converting to hex yielded nothing.

   So let's just cut and paste the displayed flag into the picoCTF window to gain the credit.... and 'lo, it worked fine.



### Side Notes

1. There isn't a recursive option within the *unzip* command. It is possible to write a script to do it, but hardly seems worth it for this challenge.
