import random

def typoglycemia(s:str) -> str:
    return ' '.join([w[0] + ''.join(random.sample(w[1:-1], len(w)-2)) + w[-1] if len(w) > 4 else w for w in s.split()])

s:str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

print(typoglycemia(s))