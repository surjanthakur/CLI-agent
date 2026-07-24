from ..common import run_script


# adjust mac sound
def adjust_sound(value: int):
    str_value = str(value)
    """this function change the sound volume"""
    script = f"set volume output volume {str_value}"
    run_script.run_process(script)


# mute sound
def mute_sound():
    "this function mute the sound"
    script = "set volume with output muted"
    run_script.run_process(script)


# unmute sound
def unmute():
    "this function unmute the sound"
    script = "set volume without output muted"
    run_script.run_process(script)


# clear recent meanu
def recent_clear_menu():
    """this function clear the menu from the recent items."""
    script = """
    tell application "System Events"
    tell application process "Finder"
    set frontmost to true
    click menu item "Clear Menu" of menu "Recent Items" of menu item "Recent Items" of menu "Apple" of menu bar item "Apple" of menu bar 1
    end tell
    end tell
    """
    run_script.run_process(script)


# put mac on sleep
def sleep_mode():
    """this function turns on mac sleep mode"""
    script = """
    tell application "System Events" 
     sleep 
    end tell
    """
    run_script.run_process(script)


# lock mac screen
def lock_screen():
    """this function lock the mac"""
    script = """
    tell application "System Events"
    keystroke "q" using {control down, command down}
    end tell
    """
    run_script.run_process(script)
