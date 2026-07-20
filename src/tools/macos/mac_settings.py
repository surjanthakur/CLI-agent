from ..common import run_script
from subprocess import SubprocessError

import subprocess


# adjust mac sound
def adjust_sound(value: int):
    """this function change the sound volume"""
    script = f"set volume output volume {str(value)}"
    run_script.run_process(script)


# mute sound
def mute_sound():
    "this function mute the sound"
    script = f"set volume with output muted"
    run_script.run_process(script)


# unmute sound
def unmute():
    "this function unmute the sound"
    script = f"set volume without output muted"
    run_script.run_process(script)


# set brightness
def set_brightness(percent: int):
    try:
        if not 0 <= percent <= 100:
            raise ValueError("Brightness must be between 0 and 100")

        value = percent / 100

        process = subprocess.Popen(
            ["brightness", str(value)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        stdout, stderr = process.communicate()

        if process.returncode != 0:
            raise RuntimeError(stderr.strip())

    except SubprocessError as err:
        print(f"error while running subprocess script: {err}")
