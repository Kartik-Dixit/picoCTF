#!/usr/bin/python3

import hashlib

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = ""
key_part_static2_trial = "}"


username_trial = b"FRASER"
index = [4,5,3,6,2,7,1,8]
dynamic_flag = []

for i in index:
	dynamic_flag.append(hashlib.sha256(username_trial).hexdigest()[i])

key_part_dynamic1_trial = "".join(dynamic_flag)
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial
print(key_full_template_trial)