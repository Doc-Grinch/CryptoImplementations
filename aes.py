from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from os import urandom

BLOCK_SIZE = 16
KEY_SIZE = 16

key = urandom(KEY_SIZE)
print(f"Key value is:\nkey = {key.hex()}")

aes = Cipher(algorithms.AES(key), modes.ECB())
aes_ecb_encryptor = aes.encryptor()

plaintext = bytes([0x00] * BLOCK_SIZE)
print(f"Plaintext value is:\nplaintext = {plaintext}")

ciphertext = aes_ecb_encryptor.update(plaintext) + aes_ecb_encryptor.finalize()
print(f"enc({plaintext.hex()}) = {ciphertext.hex()}")

aes_ecb_decryptor = aes.decryptor()
plaintext = aes_ecb_decryptor.update(ciphertext) + aes_ecb_decryptor.finalize()
print(f"dec({ciphertext.hex()}) = {plaintext.hex()}")
