# Mod 26
- Category : Cryptography
- Points 10

### Description

Cryptography can be easy, do you know what ROT13 is?. *cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_Ncualgvd}*

### Downloads
None

### Hints

1. This can be solved online if you don't want to do it by hand!

## Overview

Another simple task; but this time relying on you to figure out what to do. [Wikipedia](https://en.wikipedia.org/wiki/ROT13) is a great place to figure out what [ROT13](https://en.wikipedia.org/wiki/ROT13) is all about.

One can see that the string given in the description *cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_Ncualgvd}* seems to match the format of the picoCTF flag; aka *picoCTF{.....}* albeit that the text is encrypted.

## Steps

1. Apply the ROT13 logic to the first character of the string

```
c -> d -> e -> f -> g -> h -> i -> j -> k -> l -> m -> n -> o -> p
```

  Woo-hoo; the cipher-text *c* maps to the plain-text *p*

2. Apply the same logic to the next character - *v* - which seems to map, as required, to *i*. This definitely seems to be right way to go.

   However, performing the conversion by hand is a little tedious - so let's see if an online tool can help.

3. Using [CyberChef](https://gchq.github.io/CyberChef/#recipe=ROT13(true,true,false,13)&input=Y3ZwYlBHU3thcmtnX2d2enJfVid5eV9nZWxfMl9lYmhhcWZfYnNfZWJnMTNfTmN1YWxndmR9) provides the complete plaintext quickly and easily.

4. Cut and paste the output into the picoCTF window to gain the credit

```
picoCTF{next_time_I'll_try_2_rounds_of_rot13_*******}
```

### Side Notes

1. There are loads of ROT13 conversion tools online; many of which provide for different offset values other than 13.

2. CyberChef wasn't the first tool that I found but it certainly seems to be quite comprehensive. The lack of instructions is a bit frustrating - but it's powerful, free and has quite a pedigree! It is certainly worth investing the time to figure it out.
