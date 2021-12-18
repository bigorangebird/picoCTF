# Nice Netcat
- Category : General Skills
- Points 15

### Description

There is a nice program that you can talk to by using this command in a shell: *$ nc mercury.picoctf.net 35652*, but it doesn't speak English...

### Downloads
None

### Hints

1. You can practice using netcat with this picoGym problem: [what's a netcat?](https://play.picoctf.org/practice/challenge/34)

2. You can practice reading and writing ASCII with this picoGym problem: [Let's Warm Up](https://play.picoctf.org/practice/challenge/22)


## Overview

This task is more about reading between the lines of the hints....

## Steps

1. From the command line, run the *nc* command as instructed

```
nc mercury.picoctf.net 35652
```
   and we are presented with a list of values

```
112
105
99
111
67
84
70
123
103
48
48
100
95
107
49
116
116
121
33
95
110
49
99
51
95
107
49
116
116
121
33
95
57
98
51
98
55
51
57
50
125
10
```

2. The second hint suggests that reading ASCII would be helpful. Google is my friend ... with the [AsciiTable website](https://www.asciitable.com) providing a great, simple reference - the Wikipedia page is just too detailed to be useful for this exercise.


3. We can see that *112* (as a decimal value) maps to *p*; and *105* maps to *i* ... so this stream of values seems to be our flag encoded as ASCII values

4. Using the ['From Decimal' recipe in CyberChef] (https://gchq.github.io/CyberChef), we can quickly convert the list to our flag

```
picoCTF{g00d_k1tty!_n1c3_k1tty!_******}
```

5. Cut and paste the displayed flag into the picoCTF window to gain the credit



### Side Notes

1. Seems very odd that both of the helpful hints to this 15 point challenge take you to more advanced challenges!
