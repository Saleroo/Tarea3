import base64



import camellia


plain = b"This is a text. "
c1 = camellia.CamelliaCipher(key=b'16 byte long key', IV=b'16 byte iv. abcd', mode=camellia.MODE_CBC)
encrypted = c1.encrypt(plain)
c2 = camellia.CamelliaCipher(key=b'16 byte long key', IV=b'16 byte iv. abcd', mode=camellia.MODE_CBC)
decrypted = c2.decrypt(encrypted)
encrypted=base64.standard_b64encode(encrypted)
print(encrypted)
print(decrypted)
