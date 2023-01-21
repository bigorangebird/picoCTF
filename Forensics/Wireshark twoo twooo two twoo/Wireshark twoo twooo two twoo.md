# Wireshark twoo twooo two twoo

- Category : Forensics
- Points 100

### Description

Can you find the flag? [shark2.pcapng](https://mercury.picoctf.net/static/0fe13a33318e756f71c35cb490e64c81/shark2.pcapng).

### Downloads

[shark2.pcapng](./shark2.pcapng)

### Hints

1. Did you really find _the_ flag?

2. Look for traffic that seems suspicious.

## Overview

Need to learn to use Wireshark for this one....

## Steps

1. From the command line, run the _wget_ command to download the file

```
https://mercury.picoctf.net/static/0fe13a33318e756f71c35cb490e64c81/shark2.pcapng
```

And open with our Wireshark application

2. Using the Wireshark 'search' function, we look for _pico_ ... and notice packet 744

```
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 73
Server: Werkzeug/1.0.1 Python/3.6.9
Date: Mon, 10 Aug 2020 01:39:19 GMT

picoCTF{bfe48e8500c454d647c55a4471985e776a07b26cba64526713f43758599aa98b}
```

Seems a bit too easy .... and it does look to be hex-encoded (0-9a-f).
We also note the warning in hint 1, and continue our hunt for now.

And we also note that there are 90 packets that contain such challenge flags... all different
May be it isn't that easy after all.

3. Noting hint 2 ... we look for other network traffic that might raise an eye.

   There are four packets which seem to be _acknowledging unseen segment_ ... ie sending a ACK message for a packet that hasn't been seen. Googling the issue ... this might be OK at the start of a monitoring session.. but this is some 800 packets into the session.

   But we also see quite a number of DNS queries for some oddly named sub-domains of reddshirmpandherring.com

4. There is no website at http://www.reddshrimpandherring.com

   But I wonder if there is a message hidden in those sub-domain strings... they look it might be Base64 encoded. I just need to figure out how to extract the details .... cut'n'paste will take forever

5. Ooo - but hang on a minute - so of those queries are to/from 8.8.8.8 which is Google's DNS service; so we can apply a display filter to ignore those.

   This brings the number of 'interesting' packets down from 1512 to just 42.

   Of those, half are acknowledgements ... so we are now down to just 21.
   And we can now see that there are three queries containing the same suspected payload; so we can filter further down to just 7 records.

   Our final, after lots of reading and messing, Wireshark display filter is

   ```
   dns && (ip.src != 8.8.8.8 && ip.dst != 8.8.8.8 && ip.src != 18.217.1.57) && dns.qry.name matches ".reddshrimpandherring.com$"
   ```

   Which leaves us with

   ```
   No.	Time	Source	Destination	Protocol	Length	Info
   1633	9.334169	192.168.38.104	18.217.1.57	DNS	93	Standard query 0xdf26 A cGljb0NU.reddshrimpandherring.com
   2042	11.870534	192.168.38.104	18.217.1.57	DNS	93	Standard query 0x3a30 A RntkbnNf.reddshrimpandherring.com
   2444	14.503146	192.168.38.104	18.217.1.57	DNS	93	Standard query 0x531d A M3hmMWxf.reddshrimpandherring.com
   3140	16.404809	192.168.38.104	18.217.1.57	DNS	93	Standard query 0x99dd A ZnR3X2Rl.reddshrimpandherring.com
   3429	18.239530	192.168.38.104	18.217.1.57	DNS	93	Standard query 0x16f6 A YWRiZWVm.reddshrimpandherring.com
   3969	20.266171	192.168.38.104	18.217.1.57	DNS	89	Standard query 0xbe68 A fQ==.reddshrimpandherring.com
   4361	22.481648	192.168.38.104	18.217.1.57	DNS	89	Standard query 0xa740 A fQ==.reddshrimpandherring.com
   ```

6. We can now cut'n'paste (I can probably do something with TShark and an AWK script, but seems a lot of work for just seven records)

```
    cGljb0NU + RntkbnNf + M3hmMWxf + ZnR3X2Rl + YWRiZWVm + fQ== + fQ==

    cGljb0NURntkbnNfM3hmMWxfZnR3X2RlYWRiZWVmfQ==fQ==

```

6. Moving to CyberChef, we check whether this is our challenge flag.

Which it is

```
picoCTF{dns_3xf1l_ftw_deadbeef}}
```

Quite why there are two closing braces ... might be an issue with my filtering, so let's assume it's just one for now.

7. Cut and paste the displayed flag into the picoCTF window .... and we were right, and gain the credit

### Side Notes

None
