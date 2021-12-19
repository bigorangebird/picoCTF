# Magikarp Ground Mission
- Category : General Skills
- Points 30

### Description

Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. Login via `ssh` as `ctf-player` with the password, `b60940ca`

### Downloads
None

### Hints

1. Finding a cheatsheet for bash would be really helpful!


## Overview

Another case of following the provided instructions to get to the flag... albeit a little more complex this time, and involving spinning up a virtual machine within picoCTF


## Steps

1. Let's click on the 'Launch Instance' button

   After a few seconds, the status changes from 'Not Running', through 'Starting' to 'Running'
   A count-down timer also appears ... which seems to suggest that we have no more than an hour to complete this challenge before the instance will disappear.

   Some additional information now appears below the challenge description

    ```
    CHALLENGE ENDPOINTS
    SSH	: ssh ctf-player@venus.picoctf.net -p 54984
    ```


2. Using the provided *ssh* command, let's connect to the instance ... answering 'yes' when needed.

   ```
   > ssh ctf-player@venus.picoctf.net -p 54984
   The authenticity of host '[venus.picoctf.net]:54984 ([3.131.124.143]:54984)' can't be established.
   ED25519 key fingerprint is SHA256:P1f6h95BrSVnJbm2AKhphfHHGEyAeThib/rN/AwKs24.
   This host key is known by the following other names/addresses:
       ~/.ssh/known_hosts:19: [venus.picoctf.net]:54531
   Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
   Warning: Permanently added '[venus.picoctf.net]:54984' (ED25519) to the list of known hosts.
   ctf-player@venus.picoctf.net's password:
   ```

   and we need to supply password provided in the instructions.


3. Once logged in, we will see a shell prompt

   ```
   Welcome to Ubuntu 18.04.5 LTS (GNU/Linux 5.4.0-1041-aws x86_64)

    * Documentation:  https://help.ubuntu.com
    * Management:     https://landscape.canonical.com
    * Support:        https://ubuntu.com/advantage
   This system has been minimized by removing packages and content that are
   not required on a system that users do not log into.

   To restore this content, you can run the 'unminimize' command.

   The programs included with the Ubuntu system are free software;
   the exact distribution terms for each program are described in the
   individual files in /usr/share/doc/*/copyright.

   Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
   applicable law.

   ctf-player@pico-chall$
   ```


4. We can now follow the next instruction, and use the *ls* command to list the files in the current directory

   ```
   > ls
   1of3.flag.txt  instructions-to-2of3.txt
   ```

   And we see two files .... and it looks like there are three steps to this challenge.
   So let's see what needs to be done - and use the *cat* command to look into the files.
   ```
   > cat *
   picoCTF{xxsh_
   Next, go to the root of all things, more succinctly `/`
   ```

5. Ok, so let's follow the instructions again

   ```
   > cd /
   > ls
   2of3.flag.txt  bin  boot  dev  etc  home  instructions-to-3of3.txt  lib  lib64	media  mnt  opt  proc  root  run  sbin	srv  sys  tmp  usr  var
   ```

   Again we see two files that interest us.. so let's display their contents

   ```
   > cat *txt
   0ut_0f_\/\/4t3r_
   Lastly, ctf-player, go home... more succinctly `~`
   ```

6. Ok, so let's follow the instructions one last time

      ```
      > cd ~
      > ls
      3of3.flag.txt  drop-in
      ```

      And we see a file with final part of the flag .. so let's display it's contents

      ```
      > cat *txt
      *******}
      ```

7. So we just need to cut and paste each of the three parts into the picoCTF window to gain the credit

      picoCTF{xxsh_0ut_0f_\/\/4t3r_******}


### Side Notes

None
