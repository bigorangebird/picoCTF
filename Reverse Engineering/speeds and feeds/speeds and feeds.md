# Speeds and Feeds
- Category : Reverse Engineering
- Points 50

### Description

There is something on my shop network running at nc mercury.picoctf.net 28067, but I can't tell what it is. Can you?


### Downloads
None


### Hints

1. What language does a CNC machine use?


## Overview

The hint gives us a start ... but then a quick google for some of the strings in the service output get us to the same place as quickly.


## Steps

1. Okay... let's access the web service

   ```
   > nc mercury.picoctf.net 28067
   G17 G21 G40 G90 G64 P0.003 F50
   G0Z0.1
   G0Z0.1
   G0X0.8276Y3.8621
   G1Z0.1
   G1X0.8276Y-1.9310
   G0Z0.1
   G0X1.1034Y3.8621
   G1Z0.1
   G1X1.1034Y-1.9310
   G0Z0.1
   ...
   ```

   There is quite a bit of output, so let's capture it to a file so that we can look at in more detail

   ```
   nc mercury.picoctf.net 28067 > nc.out    
   ```

2. This looks familiar, as I've played with 3d printers .... so a quick Google search for *G1Z0* confirms my suspicion that this does indeed look like a G-code routine used to control a CNC machine.

   Hmmm - there are no comments within the file. So where is the flag?


3. Lightbulb ... I wonder if this code would plot out the flag? A quick Google search (other search engines are available :-) ) shows that there are plenty of online GCode emulators available.

   So I copied the gcode into https://ncviewer.com

   And the challenge flag appeared in the [on-screen plot](./Speeds and Feeds.png).
   *picoCTF{num3r1cal_c0ntr0l_******}*

   
4. We'll need to enter the challenge flag directly into picoCTF to gain the credit



### Side Notes

1. It might have been fun to produce this on a CNC plotter... but this was quicker!
