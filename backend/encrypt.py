# encrypt constants:
SHIFT = 5
DIRECTION = 1

def encrypt(text):
    return encryptND(text, SHIFT, DIRECTION)

def encryptND(user_password, N, D):
    text_encrypted = ''
    reversed_user = user_password[::-1]
    for i in reversed_user:
        new_ascii = (ord(i) - 34 + D * N) % 92
        new_char = chr(new_ascii + 34)
        text_encrypted += new_char

    return text_encrypted

def decrypt(text):
    return decryptND(text, SHIFT, DIRECTION)

def decryptND(encrypted_text, N, D):
    text_decrypted = ''
    reversed_user = encrypted_text[::-1]
    for i in reversed_user:
        new_ascii = (ord(i) - 34 - (D * N)) % 92
        new_char = chr(new_ascii + 34)
        text_decrypted += new_char

    return text_decrypted