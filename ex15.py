import subprocess

n : int = int(input())
subprocess.run(f"tail -n {n} popular-names.txt",shell=True)
