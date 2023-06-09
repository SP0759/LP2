import math

p = int(input("p: "))
q = int(input("q: "))
n = p * q
e = 2
k = 2
phi = (p - 1) * (q - 1)
while e < phi:
    if math.gcd(e, phi) == 1:
        break
    else:
        e += 1

d = int(((k * phi) + 1) / e)

print(f"Public Key (e, n): ({e}, {n})")
print(f"Private Key (d, n): ({d}, {n})")

msg = input("Enter your message: ")

encryptedMSG = [pow(ord(char), e, n) for char in msg]
decryptedMSG = ''.join([chr(pow(char, d, n)) for char in encryptedMSG])

print("Original string: ", msg)
print("Encrypted string: ", encryptedMSG)
print("Decrypted string: ", decryptedMSG)
