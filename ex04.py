S: str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
L: list[str] = S.replace(',','').replace('.','').split()
D: dict[str,int] = {}

for i in range(len(L)):
    if i+1 in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        D[L[i][:1]] = i+1
    else:
        D[L[i][:2]] = i+1

print(D)
