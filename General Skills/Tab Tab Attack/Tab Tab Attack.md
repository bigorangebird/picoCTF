# Tab Tab Attack
- Category : General Skills
- Points 20

### Description

Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames: [Addadshashanammu.zip](https://mercury.picoctf.net/static/fe16c756149cfa85f23e73cd9dbd6a25/Addadshashanammu.zip)

### Downloads
[Addadshashanammu.zip](./Addadshashanammu.zip)


### Hints

1. After `unzip`ing, this problem can be solved with 11 button-presses...(mostly Tab)...


## Overview

A really simple task - just follow the instructions provided in the Hints


## Steps

1. From the command line, run the *wget* command to download the file

   ```
   https://mercury.picoctf.net/static/fe16c756149cfa85f23e73cd9dbd6a25/Addadshashanammu.zip  
   ```

2. Unzip the file  

   ```
   > unzip Addadshashanammu.zip
     Archive:  Addadshashanammu.zip
        creating: Addadshashanammu/
        creating: Addadshashanammu/Almurbalarammi/
        creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/
        creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/
        creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/
        creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/
        creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/
        inflating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/fang-of-haynekhtnamet
   ```

3. Many layers of sub-directory are created - with just one file at the end of the tree

4. We can use the *strings* command. The hint tells us to use the 'TAB' key to save a lot of typing....

   TAB is the shell autocompleter ... start typing a filename and hit 'TAB' ... if only one option exists, it will autocomplete. If multiple options exists, then it will autocomplete as much as it can.

   We need to select the first

   ```
   string Add<TAB>/<TAB><TAB><TAB><TAB><TAB><TAB><TAB>
   ```

   will yield

   ```
   strings Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/fang-of-haynekhtnamet
   ```

   We can then pipe the output through *grep* to look for any lines containing *pico*

   ```
   strings Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/fang-of-haynekhtnamet | grep pico
   ```

   Which gives us the challenge key

   *ZAP!* picoCTF{l3v3l_up!_t4k3_4_r35t!_******}

5. Now we just need cut and paste the displayed flag into the picoCTF window to gain the credit



### Side Notes

1. We could have short-circuited all of this using the *zip* option *-p*; but that would defeat the lesson of challenge

  ```
  > unzip -p Addadshashanammu.zip | strings | grep pico
  *ZAP!* picoCTF{l3v3l_up!_t4k3_4_r35t!_********}
  ```
