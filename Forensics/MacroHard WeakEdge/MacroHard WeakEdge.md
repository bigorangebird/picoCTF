# MacroHard WeakEdge
- Category : Forensics
- Points 60

### Description

I've hidden a flag in this file. Can you find it? [Forensics is fun.pptm](https://mercury.picoctf.net/static/52da699e0f203321c7c90ab56ea912d8/Forensics%20is%20fun.pptm)


### Downloads
[Forensics is fun.pptm](./Forensics is fun.pptm)


### Hints

None



## Overview

Unpack & search


## Steps

1. From the command line, run the *wget* command to download the file

   ```
   https://mercury.picoctf.net/static/52da699e0f203321c7c90ab56ea912d8/Forensics%20is%20fun.pptm
   ```

2. A quick google search tells us that the .pptm file is MS Powerpoint file (which I don't have).

   We also find that it is just a compressed archive... so we can decompress it quite easily without needing a copy of MS Powerpoint.

   ```
   > tar -xvf Forensics\ is\ fun.pptm -C unpacked_pptm
   ```

3. A quick look thought the list of the filenames as they were extracted ... one named 'ppt/slideMasters/hidden' looks like it might be worth a closer look.

   ```
   > file ppt/slideMasters/hidden
   ppt/slideMasters/hidden: ASCII text, with no line terminators

   > cat ppt/slideMasters/hidden
   Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q
   ```

   Oooh, this looks like something has been encoded.

3. Let's goto CyberChef and see if we can figure it out; but first let's remove the spaces between each letter.

   The resultant text string *ZmxhZzogcGljb0NURntEMWRfdV9rbjB3X3BwdHNfcl96MXA1fQ* contains A-Za-z0-9 ... which suggests that this might be Base64 encoded.

   And yes, it is - the decoded flag being - *picoCTF{D1d_u_kn0w_ppts_r_*****}*


4. Cut and paste the flag into the picoCTF window to gain the credit



### Side Notes

1. We could have used the wireshark command line utility *tshark* but that'll take more learning from me!
