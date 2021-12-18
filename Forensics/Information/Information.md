# information
- Category : Forensics
- Points 10

### Description

Files can always be changed in a secret way. Can you find the flag? [cat.jpg](https://mercury.picoctf.net/static/a614a27d4cb251d04c7d2f3f3f76a965/cat.jpg)

### Downloads
[cat.jpg](./cat.jpg)

### Hints

1. Look at the details of the file

2. Make sure to submit the flag as picoCTF{XXXXX}



## Overview

The hints aren't exactly direct on this one ....


## Steps

1. From the command line, run the *wget* command to download the file

```
https://mercury.picoctf.net/static/a614a27d4cb251d04c7d2f3f3f76a965/cat.jpg

```

2. Trying the obvious, I opened the file in the Preview app ... and was presented with a picture of the cat. Nothing obvious was seen in the image.

3. Within Preview, I opened the Tools->Inspector utility and notice that the License was attributed to 'picoCTF'. Looks like we're on the right track and that the flag is embedded into the image meta-data; but nothing more was found within the Inspector utility.

4. I used the 'exiftool' command line utility to see if more details could be seen

```
exiftool cat.jpg       
ExifTool Version Number         : 12.36
File Name                       : cat.jpg
Directory                       : .
File Size                       : 858 KiB
File Modification Date/Time     : 2021:03:15 14:24:46-04:00
File Access Date/Time           : 2021:12:18 07:44:19-05:00
File Inode Change Date/Time     : 2021:12:18 07:44:19-05:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.02
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Current IPTC Digest             : 7a78f3d9cfb1ce42ab5a3aa30573d617
Copyright Notice                : PicoCTF
Application Record Version      : 4
XMP Toolkit                     : Image::ExifTool 10.80
License                         : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
Rights                          : PicoCTF
Image Width                     : 2560
Image Height                    : 1598
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 2560x1598
Megapixels                      : 4.1
```


5. The flag isn't immediately visible, but both the IPTC Digest and License fields seem to be encoded; IPTC seems to be in Hex and License in Base64


6. Using CyberChef to analyse the values of both fields; the flag was the plaintext from the License field.

```
picoCTF{the_m3tadata_1s_******}
```


7. Cut and paste the displayed flag into the picoCTF window to gain the credit



### Side Notes

1. An alternative image editor might well have shown the License field data in a single step; therefore negating the need to use *exiftool*

2. Not sure why they've included the instruction to wrap the flag value in picoCTF{...} as it's already presented with the wrap.
