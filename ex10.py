import subprocess

ret: str = subprocess.run(["wc", "-l","./popular-names.txt"])
print(ret)