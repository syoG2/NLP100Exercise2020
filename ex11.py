import subprocess

ret: str = subprocess.run("cat ./popular-names.txt | tr '\t' ' '",shell=True)
print(ret)