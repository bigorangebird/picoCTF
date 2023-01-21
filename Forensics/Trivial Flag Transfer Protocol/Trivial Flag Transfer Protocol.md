# MacroHard WeakEdge

- Category : Forensics
- Points 60

### Description

Figure out how they moved the [flag](https://mercury.picoctf.net/static/b686a99ec088f10b324cfe963bd32dab/tftp.pcapng).

### Downloads

[flag](./tftp.pcapng)

### Hints

1. What are some other ways to hide data?

## Overview

Steganography - a crash course!

## Steps

1. From the command line, run the _wget_ command to download the file

   ```
   https://mercury.picoctf.net/static/b686a99ec088f10b324cfe963bd32dab/tftp.pcapng
   ```

   And open it in Wireshark

2. An initial scan of the network traffic... I spotted (on line 19) a file read request.
   A good place to start ... so I added a filter to show any read requests, there were 7

   ```
   9	8.684408491	10.10.10.11	10.10.10.12	TFTP	60	Read Request, File: plan, Transfer type: octet
   11	37.013336835	10.10.10.11	10.10.10.12	TFTP	60	Read Request, File: plan, Transfer type: octet
   19	54.121134261	10.10.10.11	10.10.10.12	TFTP	60	Read Request, File: plan, Transfer type: octet
   22	59.164775845	10.10.10.11	10.10.10.12	TFTP	62	Read Request, File: program.deb, Transfer type: octet
   567	62.995474862	10.10.10.11	10.10.10.12	TFTP	63	Read Request, File: picture1.bmp, Transfer type: octet
   3790	67.595239703	10.10.10.11	10.10.10.12	TFTP	63	Read Request, File: picture2.bmp, Transfer type: octet
   146683	111.171248607	10.10.10.11	10.10.10.12	TFTP	63	Read Request, File: picture3.bmp, Transfer type: octet
   ```

3. A bit of hunting around, and wireshark can export the files for us (File -> Export Objects -> TFPT).

   Use the _file_ command to see what we've got.

   ```
   > file *
   instructions.txt: ASCII text
   picture1.bmp:     PC bitmap, Windows 3.x format, 605 x 454 x 24, image size 824464, resolution 5669 x 5669 px/m, cbSize 824518, bits offset 54
   picture2.bmp:     PC bitmap, Windows 3.x format, 4032 x 3024 x 24, image size 36578304, resolution 5669 x 5669 px/m, cbSize 36578358, bits offset 54
   picture3.bmp:     PC bitmap, Windows 3.x format, 807 x 605 x 24, image size 1466520, resolution 5669 x 5669 px/m, cbSize 1466574, bits offset 54
   plan:             ASCII text
   program.deb:      Debian binary package (format 2.0), with control.tar.gz, data compression xz
   ```

4. Let's start by looking at the contents of the two text files

   ```
   > cat instructions.txt
   GSGCQBRFAGRAPELCGBHEGENSSVPFBJRZHFGQVFTHVFRBHESYNTGENAFSRE.SVTHERBHGNJNLGBUVQRGURSYNTNAQVJVYYPURPXONPXSBEGURCYNA
   > cat plan
   VHFRQGURCEBTENZNAQUVQVGJVGU-QHRQVYVTRAPR.PURPXBHGGURCUBGBF
   ```

   Hmm, that looks like some encrypted text, so loading into CyberChef to see what we can find.
   Ok, so ROT13 gave us (spaces added for readability)

   ```
   TFTP DOESNT ENCRYPT OUR TRAFFIC SO WE MUST DISGUISE OUR FLAG TRANSFER.
   FIGURE OUT AWAY TO HIDE THE FLAG AND I WILL CHECK BACK FOR THE PLAN
   ```

   And

   ```
    I USED THE PROGRAM AND HID IT WITH - DUE DILIGENCE. CHECK OUT THE PHOTOS
   ```

5. Hmm - what program?
   Ok - let's leave that for a moment and move onto the images and open them in an image viewer

   They don't obviously display of a challenge flag - the only thing that is amiss is in _Picture1.bmp_. There is are some dark pixels in the center of the image. The look a little out of place but zooming in doesn't reveal any detail.

   There is nothing obvious in the meta-data of any of the images.

6. So, let's look at the program.deb file.

   A Google search tells us that a Debian package is just a zipped archive; so lets explode it

   ```
   > mkdir program.deb.archive
   > tar -xvf program.deb -C program.deb.archive
   x debian-binary
   x control.tar.gz
   x data.tar.xz
   ```

   So, the archive contains two more archives ... so let's explode them in the same way

   ```
   > tar -xvf control.tar.gz -C control.archive
   x ./
   x ./md5sums
   x ./control
   > tar -xvf data.tar.xz -C data.archive
   x ./
   x ./usr/
   x ./usr/share/
   x ./usr/share/doc/
   x ./usr/share/doc/steghide/
   x ./usr/share/doc/steghide/ABOUT-NLS.gz
   x ./usr/share/doc/steghide/LEAME.gz
   x ./usr/share/doc/steghide/README.gz
   x ./usr/share/doc/steghide/changelog.Debian.gz
   x ./usr/share/doc/steghide/changelog.Debian.amd64.gz
   x ./usr/share/doc/steghide/changelog.gz
   x ./usr/share/doc/steghide/copyright
   x ./usr/share/doc/steghide/TODO
   x ./usr/share/doc/steghide/HISTORY
   x ./usr/share/doc/steghide/CREDITS
   x ./usr/share/doc/steghide/BUGS
   x ./usr/share/man/
   x ./usr/share/man/man1/
   x ./usr/share/man/man1/steghide.1.gz
   x ./usr/share/locale/
   x ./usr/share/locale/ro/
   x ./usr/share/locale/ro/LC_MESSAGES/
   x ./usr/share/locale/ro/LC_MESSAGES/steghide.mo
   x ./usr/share/locale/fr/
   x ./usr/share/locale/fr/LC_MESSAGES/
   x ./usr/share/locale/fr/LC_MESSAGES/steghide.mo
   x ./usr/share/locale/de/
   x ./usr/share/locale/de/LC_MESSAGES/
   x ./usr/share/locale/de/LC_MESSAGES/steghide.mo
   x ./usr/share/locale/es/
   x ./usr/share/locale/es/LC_MESSAGES/
   x ./usr/share/locale/es/LC_MESSAGES/steghide.mo
   x ./usr/bin/
   x ./usr/bin/steghide
   ```

   Oooh ... the last line of the output (_./usr/bin/steghide_) suggest that steganography has been used to hide the flag.

   This might possibly account for the strange pixels seen in _Picture1.bmp_ ... although steganography shouldn't alter anything visible with the image, so it might just be a real something!

7. Checking out the man page _steghide_, we need a key in order to extract the message from the image .... it must be somewhere in the second _plan_ file.

   Let's give it a try ... although first I need to install steghide on my Mac, which needs MacPorts to work. Everyday is a school day

   Our best candidate is the string _DUEDILIGENCE_

   ```
   > extract -sf picture1.bmp -p "DUEDILIGENCE.CHECKOUTTHEPHOTOS"
   steghide: could not extract any data with that passphrase!
   > steghide extract -sf picture2.bmp -p "DUEDILIGENCE.CHECKOUTTHEPHOTOS"
   steghide: could not extract any data with that passphrase!
   > steghide extract -sf picture3.bmp -p "DUEDILIGENCE"
   wrote extracted data to "flag.txt".
   ```

   So nothing appears to be hidden in their first two images, but something in the third.

   ```
   > cat flag.txt
   picoCTF{h1dd3n_1n_pLa1n_51GHT_*****}
   ```

8. That looks like a complete challenge flag - so cut and paste the flag into the picoCTF window; and the credit is gained

### Side Notes

None
