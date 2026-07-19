from subprocess import SubprocessError
import subprocess


# subprocess run func
def run_process(script: str):
    """
    this function run's the subprocess for the apple-script
    """
    try:
        process = subprocess.Popen(
            ["osascript", "-e", script],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout, stderr = process.communicate()
        if process.returncode != 0:
            raise RuntimeError(stderr)
        print(stdout)

    except SubprocessError as err:
        print(f"error while running subprocess script: {err}")
