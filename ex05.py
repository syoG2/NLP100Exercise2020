def wordNgram(n: int, s: str) -> list:
    words: list[str] = s.split()
    return [words[i:i+n] for i in range(len(words) - n + 1)]

def charNgram(n: int, s: str) -> list:
    s:str = s.replace(' ', '')
    return [s[i:i+n] for i in range(len(s) - n + 1)]

s:str = "I am an NLPer"

print(wordNgram(2, s))
print(charNgram(2, s))