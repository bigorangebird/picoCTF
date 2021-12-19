# Set up the script as for the original

import hashlib
from cryptography.fernet import Fernet
import base64

username_trial = "MORTON"
bUsername_trial = b"MORTON"

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial


# No need for a subroutine ... we can do this in-line

# We know that the key will start with the content of "key_part_static1_trial"
generated_key = key_part_static1_trial;

# Then, it is simply a case of adding to that key-header each of the characters
# in each of the comparison statements

generated_key += hashlib.sha256(bUsername_trial).hexdigest()[4]
generated_key += hashlib.sha256(bUsername_trial).hexdigest()[5]
generated_key += hashlib.sha256(bUsername_trial).hexdigest()[3]
generated_key += hashlib.sha256(bUsername_trial).hexdigest()[6]
generated_key += hashlib.sha256(bUsername_trial).hexdigest()[2]
generated_key += hashlib.sha256(bUsername_trial).hexdigest()[7]
generated_key += hashlib.sha256(bUsername_trial).hexdigest()[1]
generated_key += hashlib.sha256(bUsername_trial).hexdigest()[8]


# And output the key

print(generated_key)
