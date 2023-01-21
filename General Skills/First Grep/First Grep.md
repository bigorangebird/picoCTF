# First Grep

- Category : General Skills
- Points 100

### Description

Can you find the flag in [file](https://jupiter.challenges.picoctf.org/static/515f19f3612bfd97cd3f0c0ba32bd864/file)? This would be really tedious to look through manually, something tells me there is a better way.

### Downloads

[file](./file)

### Hints

1. grep [tutorial](https://ryanstutorials.net/linuxtutorial/grep.php)

## Overview

Grep is awesome

## Steps

1. First we grab the file

   ```
   wget https://jupiter.challenges.picoctf.org/static/515f19f3612bfd97cd3f0c0ba32bd864/file
   ```

2. Then we can use the _grep_ command to look for any challenge flags that might be in that file in clear-text

```
> grep pico file
picoCTF{grep_is_good_to_find_things_****}
```

2. Submit _picoCTF{grep*is_good_to_find_things***\*\***}_ into the picoCTF window to gain the credit

### Side Notes

None
