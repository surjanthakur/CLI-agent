from subprocess import SubprocessError
import subprocess


def run_process(script: str):
    """
    this function run's the subprocess for the apple-script
    """
    try:
        process = subprocess.Popen(
            ["osascript", "-e", script],
            check=True,
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


def open_app(app_name: str):
    """this function open the mac apps"""
    script = f'tell application "{app_name}" to activate'
    run_process(script)


def close_app(app_name: str):
    """this function close the mac apps"""
    script = f'tell application "{app_name}" to activate'
    run_process(script)
