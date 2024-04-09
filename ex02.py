S: str =  "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
L: list[int] = list(map(lambda x: len(x), S.replace(',','').replace('.','').split()))

print(L)