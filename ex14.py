import subprocess

n : int = int(input())
subprocess.run(f"head -n {n} popular-names.txt",shell=True)
