S1: str = "パトカー"
S2: str = "タクシー"

S3: str = ""
for i in range(max(len(S1),len(S2))):
    if i < len(S1):
        S3 += S1[i]
    if i < len(S2):
        S3 += S2[i]
        
print(S3)