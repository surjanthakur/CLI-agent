from ..common import run_script


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
