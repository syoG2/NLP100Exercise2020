import subprocess

subprocess.run("cut -f 1 ./popular-names.txt > col1.txt",shell=True)
subprocess.run("cut -f 2 ./popular-names.txt > col2.txt",shell=True)