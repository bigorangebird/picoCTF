# Obedient Cat
- Category : General Skills
- Points 5

### Description

This file has a flag in plain sight (aka "in-the-clear"). [Download flag](https://mercury.picoctf.net/static/33996e32dce022205a6a36f69aba56f0/flag).

### Downloads
[Flag](./flag)

### Hints

1. Any hints about entering a command into the Terminal (such as the next one), will start with a '$'... everything after the dollar sign will be typed (or copy and pasted) into your Terminal.

2. To get the file accessible in your shell, enter the following in the Terminal prompt: $ wget https://mercury.picoctf.net/static/33996e32dce022205a6a36f69aba56f0/flag

3. $ man cat

## Overview

If you are familiar with working at the command line, this is a very simple task - just follow the steps as detailed in the hints. It really doesn't get any more straight forward than this.

## Steps

1. From the command line, run the *wget* command

```
wget https://mercury.picoctf.net/static/33996e32dce022205a6a36f69aba56f0/flag
```
   But the wget command isn't available. Google shows that it's available as a Homebrew package via https://brew.sh

2. Installed homebrew using the command

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

3. Installed wget

```
brew install wget
```

4. Continue with the instructions and use *wget* command

```
wget https://mercury.picoctf.net/static/33996e32dce022205a6a36f69aba56f0/flag
```

5. Get the contents of the downloaded *flag* file with the *cat* command

```
cat flag
```

6. Cut and paste the output into the picoCTF window to gain the credit

```
picoCTF{s4n1ty_v3r1f13d_*******}
```

### Side Notes

1. Wget is a free utility for non-interactive download of files from the Web.
