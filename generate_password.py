
'''
# 8 Digit random number generate
# first Digit should be Alphabet
# last Digit should be Alphabet
# Random Password should be Alpha numeric


1. A - Z random number
2. 1- 9 random number
3. I and O should be elemented
4. 1,0 should be elemeneted
 # 8-Digit Alphanumeric Code Generator
 #Uppercase Alphanumeric Code Generator
 #Unique Code Generator
'''
import random
import string

def generate_random_alpha_numeric_password(length=8):
    alphanumeric_chars = string.ascii_uppercase+string.digits
    alphanumeric_chars=alphanumeric_chars.replace("I","").replace("O",'').replace('0','').replace('1','')
    letters=string.ascii_uppercase
    code=''.join(random.choice(letters)) +''.join(random.choice(alphanumeric_chars) for _ in range(length-2)) + ''.join(random.choice(letters))
    return code


passwords=generate_random_alpha_numeric_password(8)
print(passwords)






