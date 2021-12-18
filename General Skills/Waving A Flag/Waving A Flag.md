# Waving A Flag
- Category : General Skills
- Points 10

### Description

Can you invoke help flags for a tool or binary? [This program](https://mercury.picoctf.net/static/cfea736820f329083dab9558c3932ada/warm) has extraordinarily helpful information...

### Downloads
[This program](./warm)

### Hints

1. This program will only work in the webshell or another Linux computer.

2. To get the file accessible in your shell, enter the following in the Terminal prompt: $ wget https://mercury.picoctf.net/static/cfea736820f329083dab9558c3932ada/warm

3. Run this program by entering the following in the Terminal prompt: $ ./warm, but you'll first have to make it executable with $ chmod +x warm

4. -h and --help are the most common arguments to give to programs to get more information from them!

5. Not every program implements help features like -h and --help.


## Overview

Another relatively simple task that just requires following the instructions provided in the hints.

## Steps

1. From the command line, run the *wget* command to download the file

```
https://mercury.picoctf.net/static/cfea736820f329083dab9558c3932ada/warm

```

2. Following the instruction, we need to change the permissions on the *warm* program wsing the *chmod* command  

```
chmod +x warm
```

3. Run the executable (see note 3) and checkout the output

```
./warm
Hello user! Pass me a -h to learn what I can do!
```


4. Re-run and provide the *-h* option

```
./warm -h
HOh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_*******}
```

5. Cut and paste the displayed flag into the picoCTF window to gain the credit



### Side Notes

1. Using the command  *'ls -la'* shows that the initial permissions of the *warm* executable are

```
-rw-r--r-- 1 kali kali 10936 Mar 15  2021 warm
```

   After running *chmod* it is
```
-rwxr-xr-x 1 kali kali 10936 Mar 15  2021 warm
```

2. Using the command *file* shows that this indeed an executable rather than a scripts

```
file warm
warm: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=3aa19b2a9cc4e093d64025eab8f510679b523455, with debug_info, not stripped
```

3. The instructions warn us that this program should be run via the picoCtf webshell or via a Linux shell. Initially I attempted to use my Mac's zshell but received the error

```
./warm
zsh: exec format error: ./warm
```

   Instead, I moved to my Kali VM (which runs on Debain linux), re-ran the steps to download and chmod the file.
