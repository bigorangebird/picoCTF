# Vault-door-training
- Category : Reverse Engineering
- Points 50

### Description

Your mission is to enter Dr. Evil's laboratory and retrieve the blueprints for his Doomsday Project. The laboratory is protected by a series of locked vault doors. Each door is controlled by a computer and requires a password to open. Unfortunately, our undercover agents have not been able to obtain the secret passwords for the vault doors, but one of our junior agents obtained the source code for each vault's computer! You will need to read the source code for each level to figure out what the password is for that vault door. As a warmup, we have created a replica vault in our training facility. The source code for the training vault is here: [VaultDoorTraining.java](https://jupiter.challenges.picoctf.org/static/03c960ddcc761e6f7d1722d8e6212db3/VaultDoorTraining.java)


### Downloads
[VaultDoorTraining.java](./VaultDoorTraining.java)


### Hints

1. The password is revealed in the program's source code.


## Overview

Not exactly the toughest of challenges so far ... and doesn't really seem worthy of 50 points, if I'm honest.


## Steps

1. Okay... let's grab the supplied file with wget

   ```
   wget https://jupiter.challenges.picoctf.org/static/03c960ddcc761e6f7d1722d8e6212db3/VaultDoorTraining.java
   ```


2. We open the file in a text editor and see this at the end...

   ```
   public boolean checkPassword(String password) {
       return password.equals("w4rm1ng_Up_w1tH_jAv4_3808******");
   }
   ```

   Which seems to tell us all we need to know, just need to wrap it with *picoCTF{...}*


3. Cut and paste the displayed flag, and adding the closing brace into the picoCTF window to gain the credit



### Side Notes

None
