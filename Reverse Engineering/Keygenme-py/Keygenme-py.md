# Keygenme-py
- Category : Reverse Engineering
- Points 30

### Description

[keygenme-trial.py](https://mercury.picoctf.net/static/0c363291c47477642c72630d68936e50/keygenme-trial.py)


### Downloads
[keygenme-trial.py](./keygenme-trial.py)


### Hints

None


## Overview

Need to figure this out from scratch


## Steps

1. Okay... so no description and no hints! So, let's grab the supplied file with wget

   ```
   wget https://mercury.picoctf.net/static/0c363291c47477642c72630d68936e50/keygenme-trial.py  
   ```


2. Opening the file in a text editor shows

   ```
   16: username_trial = "MORTON"
   17: bUsername_trial = b"MORTON"
   18:
   19: key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
   20: key_part_dynamic1_trial = "xxxxxxxx"
   21: key_part_static2_trial = "}"
   22: key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial
   ```

   There sees to be a challenge flag embedded in the code ... but extracting and combining failed to produce a valid key when uploaded into picoCTF.


3. So let's run the script and see what we get

   ```
   > python3 keygenme-trial.py

   ===============================================
   Welcome to the Arcane Calculator, MORTON!

   This is the trial version of Arcane Calculator.
   The full version may be purchased in person near
   the galactic center of the Milky Way galaxy.
   Available while supplies last!
   =====================================================


   ___Arcane Calculator___

   Menu:
   (a) Estimate Astral Projection Mana Burn
   (b) [LOCKED] Estimate Astral Slingshot Approach Vector
   (c) Enter License Key
   (d) Exit Arcane Calculator
   What would you like to do, MORTON (a/b/c/d)?   
   ```

   So it would appear that we need to enter a valid licence key to unlock option (b)


4. Back to our editor, we notice that if the user selects option c,

   ```
   87: elif choice == "c":
   88:   enter_license()
   ```

   which, after accepting the license key input, performs some checks

   ```
   134: if check_key(user_key, bUsername_trial):
   135:     decrypt_full_version(user_key)
   136: else:
   137:     print("\nKey is NOT VALID. Check your data entry.\n\n")
   ```

   The check_key function seems to have a number of checks included... which we can reverse engineer.


5. Let's take a look at the component parts of the checks to inform the reverse engineering task

   Firstly, that the length of key input is the same the length of the template key (defined on line 22) ... which happens to be 32 characters.

   ```
   144: if len(key) != len(key_full_template_trial):
   ```

   Secondly, that the initial part of the file matches exactly the text contained in the variable *key_part_static1_trial* (defined on line 19).

   ```
   148: i = 0
   149: for c in key_part_static1_trial:
   150:     if key[i] != c:
   151:         return False
   152:
   153:     i += 1
   ```

   So we know that the license key starts with *picoCTF{*

   Then, between lines 157 and 193, the function checks that the input matches a mixed-order list of the *user_name* characters .... characters that have been hashed.

   In pseudo-code; the reverse engineer will look like
   ```
   generated_key = key_part_static1_trial;

   generated_key += hash(user_name)[4]
   generated_key += hash(user_name)[5]
   generated_key += hash(user_name)[3]
   generated_key += hash(user_name)[6]
   generated_key += hash(user_name)[2]
   generated_key += hash(user_name)[7]
   generated_key += hash(user_name)[1]
   generated_key += hash(user_name)[8]

   print(generated_key)
   ```

6. Running the reverse-engineering script

   ```
   > python3 reverse.py
   picoCTF{1n_7h3_|<3y_of_******
   ```

   So we are just missing the closing brace

5. Cut and paste the displayed flag, and adding the closing brace into the picoCTF window to gain the credit



### Side Notes

1. We didn't need to input the key into the running script to unlock and be able to use the "Estimate Astral Slingshot Approach Vector" after all.
