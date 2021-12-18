# Static ain't always noise
- Category : General Skills
- Points 20

### Description

Can you look at the data in this binary: [static](https://mercury.picoctf.net/static/7495259e963bd5b67d0fb8b616652618/static)? This [BASH script](https://mercury.picoctf.net/static/7495259e963bd5b67d0fb8b616652618/ltdis.sh) might help!

### Downloads
[static](./static)
[bash script](./ltdis.sh)


### Hints

None


## Overview

Another relatively simple task.

## Steps

1. From the command line, run the *wget* command to download the files

   ```
   > wget https://mercury.picoctf.net/static/7495259e963bd5b67d0fb8b616652618/static
   > wget https://mercury.picoctf.net/static/7495259e963bd5b67d0fb8b616652618/ltdis.sh
   ```

2. We're told to run the script *ltdis.sh* but my shell doesn't want to know.
   We need to add the execute permission using *chmod* again

   ```
   > chmod +x ltdis.sh
   ```

3. Running the script again, we see an error followed by some usage help text

   ```
   Attempting disassembly of  ...
   /Library/Developer/CommandLineTools/usr/bin/objdump: error: 'a.out': No such file or directory
   Disassembly failed!
   Usage: ltdis.sh <program-file>
   Bye!
   ```


4. Re-running with the provided binary....

   ```
   > ./ltdis.sh static
   Attempting disassembly of static ...
   Disassembly successful! Available at: static.ltdis.x86_64.txt
   Ripping strings from binary with file offsets...
   Any strings found in static have been written to static.ltdis.strings.txt with file offset
   ```


5. We could open the output file and scan manually for the challenge flag; or we could automate it with the *grep* command

      ```
      > grep pico static.ltdis.strings.txt  
      1020 picoCTF{d15a5m_t34s3r_***}
      ```


5. All that is left is to cut and paste the displayed flag into the picoCTF window to gain the credit



### Side Notes

None
