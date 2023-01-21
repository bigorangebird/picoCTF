# Hurry up! Wait!

- Category : Reverse Engineering
- Points 100

### Description

[svchost.exe](https://mercury.picoctf.net/static/7163c5d64bc60b4d079422da5c5e5053/svchost.exe)

### Downloads

[svchost.exe](./svchost.exe)

### Hints

None

## Overview

Wow ... literally help here whatsoever.

## Steps

1. Okay... let's get a copy of the file with _wget_ and see what it is

   ```
   > file svchost.exe
   svchost.exe: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=4c4687ba4c5b7fea4c9f13aaa29269a3ca164b09, stripped
   ```

   So, it's an executable .... not something I'm familiar with interogating.
   I wonder if _strings_ might tell us anything.

   Not much... I've only included the things that jumped out

   ```
   > strings svchost.exe
   ...
   libgnat-7.so.1
   ...
   123456789abcdefghijklmnopqrstuvwxyzCTF_{}
   ```

2. So _libgnat_ is something to do with the ADA language ... but it doesn't seem to be available to download for either my Mac or for Debain (which is running Kali). I don't how if it's needed tho.

Then the seems to be a list of 1-9a-z characters defined somewhere; along with the text "CTF" .... and whilst I doubt it's our challenge flag, I gave it a try .... only to have it rejected.

3. I've spend ages looking at reviews of various reverse-engineering tools; and after playing with a couple, settled on [_Ghidra_](https://ghidra-sre.org).

   And an equally long time reading and learning about it.

4. After loading _svchost.exe_ into _Ghidra_ and running the 'analyse' function; I noticed that there was an 'entry' function ... which I guess is the equivalent of "main".

```
void entry(undefined8 param_1,undefined8 param_2,undefined8 param_3)
{
  undefined8 in_stack_00000000;
  undefined auStack8 [8];

  __libc_start_main(FUN_00101fcc,in_stack_00000000,&stack0x00000008,FUN_00102a30,FUN_00102aa0,
                    param_3,auStack8);
  do {
                    /* WARNING: Do nothing block with infinite loop */
  } while( true );
}
```

Which seems to do something with _\_\_libc_start_main_ and then (as the comment confirms) blocks with an infinite loop (on the _while true_)

This would align with the challenge title of 'hurry-up and wait'.

So let's explore this further.

5. _\_\_libc_start_main_ seems call a number of other functions ... we could follow those individually, but I'm pretty sure we'd be led a merry-dance.

   To let's have a more detailed look at the functions found by Ghidra to see if these is anything that catches our eye (not that we really know what we are looking at)

   The one that really stands out is _FUN_0010298a()_ ... which seems to make a long list of calls to other functions.

   ```
   void FUN_0010298a(void)

   {
     ada__calendar__delays__delay_for(1000000000000000);
     FUN_00102616();
     FUN_001024aa();
     FUN_00102372();
     FUN_001025e2();
     FUN_00102852();
     FUN_00102886();
     FUN_001028ba();
     FUN_00102922();
     FUN_001023a6();
     FUN_00102136();
     FUN_00102206();
     FUN_0010230a();
     FUN_00102206();
     FUN_0010257a();
     FUN_001028ee();
     FUN_0010240e();
     FUN_001026e6();
     FUN_00102782();
     FUN_001028ee();
     FUN_00102206();
     FUN_00102372();
     FUN_00102136();
     FUN_001023a6();
     FUN_00102136();
     FUN_0010230a();
     FUN_001023da();
     FUN_00102956();
     return;
   }
   ```

6. Looking at the first of those called functions _FUN_00102616_

   It seems to retrieve, and return, a data value ....

   ```
   void FUN_00102616(void)
   {
     ada__text_io__put__4(&DAT_00102cd8,&DAT_00102cb8);
     return;
   }
   ```

   And the contents of _&DAT_00102cd8_ seems to contain the letter _p_

   ```
   DAT_00102cd8          XREF[3]:     FUN_00102616:0010261f(*),
                                      FUN_00102616:0010262d(*),
                                      FUN_00102616:00102636(*)
          00102cd8 70              ??         70h    p
   ```

   The second function _FUN_001024aa_ reference _&DAT_00102cd1&_ which seems to contain the letter _I_

7. We might be onto something here.... I notice that there is a scripting language for Ghidra, but this seems simple enough to work through by hand.

```
  FUN_00102616();  references &DAT_00102cd8 = p
  FUN_001024aa();  references &DAT_00102cd1 = i
  FUN_00102372();  references &DAT_00102ccb = c
  FUN_001025e2();  references &DAT_00102cd7 = o
  FUN_00102852();  references &DAT_00102ce3 = C
  FUN_00102886();  references &DAT_00102ce4 = T
  FUN_001028ba();  references &DAT_00102ce5 = F
  FUN_00102922();  references &DAT_00102ce7 = {
  FUN_001023a6();  references &DAT_00102ccc = d
  FUN_00102136();  references &DAT_00102cc0 = 1
  FUN_00102206();  references &DAT_00102cc4 = 5
  FUN_0010230a();  references &DAT_00102cc9 = a
  FUN_00102206();  references &DAT_00102cc4 = 5
  FUN_0010257a();  references &DAT_00102cd5 = m
  FUN_001028ee();  references &DAT_00102ce6 = _
  FUN_0010240e();  references &DAT_00102cce = f
  FUN_001026e6();  references &DAT_00102cdc = t
  FUN_00102782();  references &DAT_00102cdf = w
  FUN_001028ee();  references &DAT_00102ce6 = _
  FUN_00102206();  references &DAT_00102cc4 = 5
  FUN_00102372();  references &DAT_00102cd1 = c
  FUN_00102136();  references &DAT_00102cc0 = 1
  FUN_001023a6();  references &DAT_00102cc0 = d
  FUN_00102136();  references &DAT_00102cc0 = 1
  FUN_0010230a();  references &DAT_00102cc9 = a
  FUN_001023da();  references &DAT_00102ccd = e
  FUN_00102956();  references &DAT_00102ce8 = }
```

Which would appear to be a challenge flag

```
picoCTF{d15a5m_ftw_5c1d1ae}
```

4. This looks a little odd, but doesn't appear to be encoded in anything obvious so we'll to enter the challenge flag directly into picoCTF abd see if we gain the credit ... which we do.

### Side Notes

1. That was a bit of a fiddle - will definitely need to look into scripting within Ghidra in the future.
