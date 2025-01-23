# Created by docgrinch the 23/01/2025
# Implementation of AES Cipher Block Chaining
# Based on the work of Jean-Philippe Aumasson from Serious Cryptography
# Version 1.0
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from os import urandom

BLOCK_SIZE = 16
KEY_SIZE = 16

# used to split the plain in 16 bytes (a block size)
def blocks(data):
    split = [data[i:i+BLOCK_SIZE].hex() for i in range(0, len(data), BLOCK_SIZE)]
    return ' '.join(split)

# generate our key
key = urandom(KEY_SIZE)
print(f"Key value = {key.hex()}")

# for CBC, need an IV for the first block
iv = urandom(KEY_SIZE)
print(f"IV value = {iv.hex()}")

# instance of AES CBC
aes = Cipher(algorithms.AES(key), modes.CBC(iv))
aes_cbc_encryptor = aes.encryptor()

# 16 bytes plain
plaintext = bytes([0x00] * BLOCK_SIZE)
print(f"Plaintext value = {plaintext}")

# encryption
ciphertext = aes_cbc_encryptor.update(plaintext) + aes_cbc_encryptor.finalize()
print(f"enc({blocks(plaintext)}) = {blocks(ciphertext)}")

# new IV to show difference with AES ECB
iv = urandom(KEY_SIZE)
print(f"IV value = {iv.hex()}")

# ecnryption with new IV but same key and plain
aes = Cipher(algorithms.AES(key), modes.CBC(iv))
aes_cbc_encryptor = aes.encryptor()
ciphertext = aes_cbc_encryptor.update(plaintext) + aes_cbc_encryptor.finalize()
print(f"enc({blocks(plaintext)}) = {blocks(ciphertext)}")

