# Tunn3l V1s10n
- Category : Forensics
- Points 30

### Description

We found this [file](https://mercury.picoctf.net/static/06a5e4ab22ba52cd66a038d51a6cc07b/tunn3l_v1s10n). Recover the flag.

### Downloads
[tunn3l_v1s10n](./tunn3l_v1s10n)

### Hints

1. Weird that it won't display right...



## Overview

Need to figure out the starting point for this one ... the hint suggest that this might be an image file.


## Steps

1. From the command line, run the *wget* command to download the file

   ```
   https://mercury.picoctf.net/static/06a5e4ab22ba52cd66a038d51a6cc07b/tunn3l_v1s10n
   ```

2. Let's use *exiftool* to see if we can gain a little more information

   ```
   > exiftool tunn3l_v1s10n
   ExifTool Version Number         : 12.36
   File Name                       : tunn3l_v1s10n
   Directory                       : .
   File Size                       : 2.8 MiB
   File Modification Date/Time     : 2021:03:15 14:24:47-04:00
   File Access Date/Time           : 2021:12:19 08:11:48-05:00
   File Inode Change Date/Time     : 2021:12:19 08:11:48-05:00
   File Permissions                : -rw-r--r--
   File Type                       : BMP
   File Type Extension             : bmp
   MIME Type                       : image/bmp
   BMP Version                     : Unknown (53434)
   Image Width                     : 1134
   Image Height                    : 306
   Planes                          : 1
   Bit Depth                       : 24
   Compression                     : None
   Image Length                    : 2893400
   Pixels Per Meter X              : 5669
   Pixels Per Meter Y              : 5669
   Num Colors                      : Use BitDepth
   Num Important Colors            : All
   Red Mask                        : 0x27171a23
   Green Mask                      : 0x20291b1e
   Blue Mask                       : 0x1e212a1d
   Alpha Mask                      : 0x311a1d26
   Color Space                     : Unknown (,5%()
   Rendering Intent                : Unknown (826103054)
   Image Size                      : 1134x306
   Megapixels                      : 0.347
   ```

   Hmm, ok - so it looks to be a BMP image file.

3. Try opening the file in an image editor - and we get an error reported around the BMP header not being valid.

  Ok - so what is wrong? Let's check out the [file format specification](https://en.wikipedia.org/wiki/BMP_file_format)

  Nothing seems wrong in the formatting of the header - but two of the length values look wrong ... the header length and the file size.

  The BMP header, according to the specification should be 14 bytes; and the DIB header should be 40 bytes ... and total of 54 bytes (36 in hex) ... not BA D0 (47824 in decimal).

  If the image is 1134 pixels wide x 306 pixels high, then at 3 bytes per pixel (bit depth = 24) then we'd expect the file size to be a little more than (1134 x 306 x 3) 1Mb in size ... but it's nearly 3Mb.


5. So, using a hex editor, we can change the header size - 4 bytes starting at 0xA - from BA D0 to 36 00

   It looks like we need to correct the image width setting in the header.

   The actual size of the BMP file is encoded in the header - offset 2, and is 4 bytes in length.

   Using *hexedit* we open the file and read the size data .... 8E 26 2c 00
   We must invert this representation as it's little-endian encoded ... 00 2c 26 8e
   Which is 2,893,454 bytes

   The specification tells us that each row of pixels is stored in 4-byte blocks ... so we must padd the row-size accordingly. Giving us a row size of 1136 bytes (1134 + (1134 % 4))

   The image height should, therefore, be 2,893,454 / (1136 x 3) bytes ... so the height will be 850
   Which is 03 52 in hex
   Encoded for little endian is 52 03


6. Looking at the specification for BMP once more, we see that the height is a 2 byte value located at 0x16.
   The current value of that location is 01 32 ... which is 306 in decimal... which is what we see in the exiftool output, so this is right location.

   We edit the value to be 52 03


7. Opening the file in an image viewer show a lovely scene ... and our challenge flag right at the top of the image.

    picoCTF{qu1t3_a_v13w_******}


8. Cut and paste the acquired flag into the picoCTF window to gain the credit.



### Side Notes

1. There isn't a recursive option within the *unzip* command. It is possible to write a script to do it, but hardly seems worth it for this challenge.
