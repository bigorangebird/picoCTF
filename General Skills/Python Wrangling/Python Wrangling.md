# Python Wrangling
- Category : General Skills
- Points 10

### Description

Python scripts are invoked kind of like programs in the Terminal... Can you run [this Python script](https://mercury.picoctf.net/static/b351a89e0bc6745b00716849105f87c6/ende.py) using [this password](https://mercury.picoctf.net/static/b351a89e0bc6745b00716849105f87c6/pw.txt) to get [the flag](https://mercury.picoctf.net/static/b351a89e0bc6745b00716849105f87c6/flag.txt.en)?

### Downloads
[Python script](./ende.py)
[Script Password](./pw.txt)
[Encrypted Flag](./flag.txt/en)

### Hints

1. Get the Python script accessible in your shell by entering the following command in the Terminal prompt: $ wget https://mercury.picoctf.net/static/b351a89e0bc6745b00716849105f87c6/ende.py

2. $ man python

## Overview

The hints are getting a little less direct now; but this is still a very straight forward task of downloading and running a Python script to obtain the flag.

## Steps

1. From the command line, run the *wget* command to download each of the three files

```
wget https://mercury.picoctf.net/static/b351a89e0bc6745b00716849105f87c6/ende.py
wget https://mercury.picoctf.net/static/b351a89e0bc6745b00716849105f87c6/pw.txt
wget https://mercury.picoctf.net/static/b351a89e0bc6745b00716849105f87c6/flag.txt.en
```

2. Using the *cat* command, we can take a quick look at the contents of each of the downloaded files.

```
cat ende.py
cat pw.txt
cat flag.txt.en
```

   The *flag.txt.en* file seems to be encrypted with something a little more complex than the ROT cypher we've just seen.

   *ende.py* seems to be Python script that we'll need to run. The beginning of the script seems to include a usage help message that will be displayed if invalid arguments are provided.

   *pw.txt* seems to be a password



3. Ran the python script file *ende.py* to see what the usage instruction tell us

```
python3 ende.py
Usage: ende.py (-e/-d) [file]
```


4. So we can re-run the script with the *-d* option (presumably for *decode*) and, presumably, the encrypted filename rather than the password file

```
python3 ende.py -d flag.txt.en
```

5. We are then prompted to enter the password, that we obtained earlier from the file *pw.txt*

```
python3 ende.py -d flag.txt.en
Please enter the password:
```

6. The flag is then decrypted and displayed. Cut and paste it into the picoCTF window to gain the credit

```
python3 ende.py -d flag.txt.en
Please enter the password:67c6cc9667c6cc9667c************
picoCTF{4p0110_1n_7h3_h0us3_******}
```

### Side Notes

1. We can use command shell pipelines to automate the input of the password into the script

```
cat pw.txt| python3 ende.py -d flag.txt.en
Please enter the password:picoCTF{4p0110_1n_7h3_h0us3_******}
```

  The output is not quite as pretty, but it does save us a little effort.
