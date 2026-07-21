from ..tools.macos import mac_settings
from ..utils.exceptions import handle_exceptions

import typer

app = typer.Typer()


# change sound
@app.command("sound", help="Change system sound volume")
def change_sound(value: int = typer.Argument(..., help="Volume level (0-100)")):
    handle_exceptions(mac_settings.adjust_sound, value)


# mute sound
@app.command("mute", help="Mute system sound")
def mute_sound():
    handle_exceptions(mac_settings.mute_sound)


# unmute sound
@app.command("unmute", help="Unmute system sound")
def unmute_sound():
    handle_exceptions(mac_settings.unmute)


# clear system menu
@app.command("clear", help="Clear the recent system menu entries")
def clear_menu(target: str = typer.Argument(..., help="pass target: menu")):
    if target:
        handle_exceptions(mac_settings.recent_clear_menu)
    typer.Exit()


# put mac on sleep mode
@app.command("sleep", help="Put the system to sleep")
def sleep_mode():
    handle_exceptions(mac_settings.sleep_mode)


# lock the screen
@app.command("lock", help="lock the system")
def lock_mode():
    handle_exceptions(mac_settings.lock_screen)
