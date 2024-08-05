def rot13(text):
    result = []
    for char in text:
        if 'A' <= char <= 'Z':
            result.append(chr((ord(char) + ord('A')) % 26 + ord('A')))
        elif 'a' <= char <= 'z':
            result.append(chr((ord(char) + ord('a')) % 26 + ord('a')))
        else:
            result.append(char)

    return ''.join(result)

# Contoh
text = "Mzzqq"
print("Encrypted", rot13(text))
decrypted = rot13(text)
print("Decrypted", decrypted)