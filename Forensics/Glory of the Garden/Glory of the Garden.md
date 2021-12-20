# Glory of the Garden
- Category : Forensics
- Points 50

### Description

This [garden](https://jupiter.challenges.picoctf.org/static/4153422e18d40363e7ffc7e15a108683/garden.jpg) contains more than it seems.

### Downloads
[garden](./garden.jpg)

### Hints

1. What is a hex editor?



## Overview

The hint seems a little off-beat for this challenge.


## Steps

1. From the command line, run the *wget* command to download the file

```
https://jupiter.challenges.picoctf.org/static/4153422e18d40363e7ffc7e15a108683/garden.jpg

```

2. Trying the obvious, I opened the file in the Preview app ... and was presented with a picture of the garden. Nothing obvious was seen in the image.

   Hardly surprising given that the hint involves using a hexeditor.


3. Opened the file using a hexeditor .... but nothing obvious at the top of the file. Started scrolling down; but this is a long file....

   So exited the hexeditor and tried
   ```
   > strings garden.jpg | grep -i pico
   Here is a flag "picoCTF{more_than_m33ts_the_3y3*******}"
   ```

   Hmm - perhaps I can search in hexedit...? Yes, I can... although it took me a while to figure out how
   to search in the ASCII rather than the hex data.

   Either way, the result is the same.


4. Cut and paste the displayed flag into the picoCTF window to gain the credit



### Side Notes

None
