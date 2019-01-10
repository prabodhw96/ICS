P = 23 # Prime no. (known to public)
G = 5 # Base (known to public)
print("Value of P: ", P)
print("Value of G: ", G)
a = 6
print("Alice's private key: ", a)
b = 15
print("Bob's private key: ", b)
x = (G**a)%P
y = (G**b)%P
# Generating secret key after exchange of keys
ka = (y**a)%P
kb = (x**b)%P
print("Secret key of Alice is: ", ka)
print("Secret key of Bob is: ", kb)

