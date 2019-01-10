from math import sqrt
def prime(pr):
    for i in range(2, int(sqrt(pr))):
        if pr%i == 0:
            return False
    return True

def gcd(x, y):
    while(y):
        x, y = y, x % y 
    return x

import sys
def calc_key(phi):
    t = phi+1
    for i in range(2, phi):
        if prime(i) and t%i == 0:
            e = i
            d = int(t/e)
            return e, d
        if i == phi-1:
            sys.exit("Can't compute keys for existing prime nos.")

p = 131
q = 139
n = p*q
phi = (p-1)*(q-1)
e, d = calc_key(phi)
msg = 18209
encrypt_msg = pow(msg, e, n)
decrypt_msg = pow(encrypt_msg, d, n)

print("Original Message: ", msg)
print("Encryption Key: ", e)
print("Decryption Key: ", d)
print("Encrypted Message: ", encrypt_msg)
print("Decrypted Message: ", decrypt_msg)

# Note: msg < n
# As n increases, msg << n