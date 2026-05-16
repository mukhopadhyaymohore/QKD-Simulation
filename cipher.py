import base64

def xor_encrypt(message, key):
    if not key:
        return ""
    key_stream = (key * ((len(message) // len(key)) + 1))[:len(message)]
    encrypted_bytes = bytes([ord(m) ^ int(k) for m, k in zip(message, key_stream)])
    return base64.b64encode(encrypted_bytes).decode("utf-8")

def xor_decrypt(ciphertext, key):
    if not key:
        return ""
    encrypted_bytes = base64.b64decode(ciphertext)
    key_stream = (key * ((len(encrypted_bytes) // len(key)) + 1))[:len(encrypted_bytes)]
    decrypted = "".join(chr(b ^ int(k)) for b, k in zip(encrypted_bytes, key_stream))
    return decrypted
