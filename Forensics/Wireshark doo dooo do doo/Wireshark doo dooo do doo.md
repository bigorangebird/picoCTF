# Wireshark doo dooo do doo
- Category : Forensics
- Points 50

### Description

Can you find the flag? [shark1.pcapng](https://mercury.picoctf.net/static/b44842413a0834f4a3619e5f5e629d05/shark1.pcapng)

### Downloads
[shark1.pcapng](./shark1.pcapng)

### Hints

None



## Overview

Need to learn to use Wireshark for this one....


## Steps

1. From the command line, run the *wget* command to download the file

```
https://mercury.picoctf.net/static/b44842413a0834f4a3619e5f5e629d05/shark1.pcapng

```

2. Download Wireshark from https://www.wireshark.org/#download

   And do a lot of reading (and watching - the Youtube videos) at https://www.wireshark.org/docs/


3. A quick search doesn't return any matches for *pico* or *ctf*; so the challenge flag is going to take a bit of work to find.

   There is a lot of information to wade through - so let's start by filtering and see if we can narrow down the search.

4. I started by looking at the http traffic - for no particular reason other than I sort-of-know-what-to-expect when looking at the records.

  There is a lot of kerberos-session-encrypted entries; and a lot of traffic related to WSMAN ... so let's filter these out for now.

  I used the automated filter-builder function within wireshark to create filters (select a message that we want filter away ... pick a field that identifies that 'type' of message ... right click and choose 'filter NOT selected').

```
http && !(http.request.uri == "/wsman/subscriptions/EB489718-F373-4F7F-8493-B0D1503B3C3E/36") && !(http.content_type == "multipart/encrypted;protocol=\"application/HTTP-Kerberos-session-encrypted\";boundary=\"Encrypted Boundary\"")
```

  And we are left with just four records
```
823	7.187055	192.168.38.104	18.222.37.134	HTTP	501	GET / HTTP/1.1
962	18.241554	192.168.38.104	169.254.169.254	HTTP	235	GET /latest/meta-data/instance-action HTTP/1.1
964	18.242484	169.254.169.254	192.168.38.104	HTTP	311	HTTP/1.0 200 OK  (text/plain)
827	7.236537	18.222.37.134	192.168.38.104	HTTP	384	HTTP/1.1 200 OK  (text/html)
```

  Checking each out in turn, the last message contains a payload of

```
Gur synt vf cvpbPGS{c33xno00_1_f33_h_qrnqorrs}
```

  The last part of which suspiciously like a challenge flag - albeit encoded.


6. Moving to CyberChef, we can pay with some decoding options.

  The string looks like it might be ROT encoded.... so we start with that and play with the offset, checking each in turn.

  It turns out we didn't need to do much - as CyberChef starts with an offset of 13 - which immediatley decoded the flag

```
picoCTF{p33kab00_1_s33_u_*******}
```


7. Cut and paste the displayed flag into the picoCTF window to gain the credit



### Side Notes

1. We could have used the wireshark command line utility *tshark* but that'll take more learning from me!
