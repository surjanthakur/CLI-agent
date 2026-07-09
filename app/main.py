import subprocess

res = subprocess.run(["python3", "--version"], capture_output=True, text=True)
print(res.stdout, res.returncode)
