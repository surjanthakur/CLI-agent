import subprocess

print("a")  # 1

res = subprocess.Popen(
    ["python3", "--version"],
    text=True,
)

res.stdout

print("b")  # 2
