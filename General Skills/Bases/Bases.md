# Bases

- Category : General Skills
- Points 100

### Description

What does this _bDNhcm5fdGgzX3IwcDM1_ mean? I think it has something to do with bases.

### Downloads

None

### Hints

1. Submit your answer in our flag format. For example, if your answer was 'hello', you would submit 'picoCTF{hello}' as the flag.

## Overview

Have you been paying attention?

## Steps

1. The string is using A-Za-z0-9 ... so it might well be base 64.
   Using CyberChef with the Base64 recipes confirms that the text decodes to

   _l3arn_th3_r0p35_

   Certainly looks reasonable ... so we wrap with _picoCTf{....}_ and submit into picoCTF

2. Yes, it's correct, so we gain the credit

### Side Notes

None
