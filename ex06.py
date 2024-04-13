def wordNgram(n: int, s: str) -> set:
    words: list[str] = s.split()
    return {words[i:i+n] for i in range(len(words) - n + 1)}

def charNgram(n: int, s: str) -> set:
    s = s.replace(' ', '')
    return {s[i:i+n] for i in range(len(s) - n + 1)}

s1: str = "paraparaparadise"
s2: str = "paragraph"

X: set = charNgram(2, s1)
Y: set = charNgram(2, s2)

print(X | Y)
print(X & Y)
print(X - Y)
print(Y - X)
print('se' in X)
print('se' in Y)