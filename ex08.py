def cipher(s):
    return ''.join([chr(219 - ord(c)) if c.islower() else c for c in s])


encode = cipher("the quick brown fox jumps over the lazy dog")
print("暗号化:",encode)
decode = cipher(encode)
print("復号化:",decode)