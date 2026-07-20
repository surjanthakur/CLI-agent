import subprocess
from subprocess import SubprocessError


def install_brightness():
    try:
        process = subprocess.Popen(
            ["brew", "install", "brightness"],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout, stderr = process.communicate()

        if process.returncode != 0:
            raise RuntimeError(stderr)

    except SubprocessError as err:
        print(f"error while running subprocess script: {err}")
