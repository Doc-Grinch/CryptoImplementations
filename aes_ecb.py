# Created by docgrinch the 23/01/2025
# Implementation of AES Electronic Codebook
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from os import urandom

BLOCK_SIZE = 16
KEY_SIZE = 16

# generate our key
key = urandom(KEY_SIZE)
print(f"Key value is:\nkey = {key.hex()}")

aes = Cipher(algorithms.AES(key), modes.ECB())
aes_ecb_encryptor = aes.encryptor()

# 16 bytes plain
plaintext = bytes([0x00] * BLOCK_SIZE)
print(f"Plaintext value is:\nplaintext = {plaintext}")

# encryption
ciphertext = aes_ecb_encryptor.update(plaintext) + aes_ecb_encryptor.finalize()
print(f"enc({plaintext.hex()}) = {ciphertext.hex()}")

# decryption
aes_ecb_decryptor = aes.decryptor()
plaintext = aes_ecb_decryptor.update(ciphertext) + aes_ecb_decryptor.finalize()
print(f"dec({ciphertext.hex()}) = {plaintext.hex()}")

# the problem with ECB => two block cipher having the same key will provide the same ciphertext
def blocks(data):
    split = [data[i:i+BLOCK_SIZE].hex() for i in range(0, len(data), BLOCK_SIZE)]
    return ' '.join(split)

plaintext = bytes([0x00] * 2 * BLOCK_SIZE)

aes = Cipher(algorithms.AES(key), modes.ECB())
aes_ecb_encryptor = aes.encryptor()

ciphertext = aes_ecb_encryptor.update(plaintext) + aes_ecb_encryptor.finalize()
print(f"enc({blocks(plaintext)}) = {blocks(ciphertext)}")


