from ..tools.macos import mac_settings

import typer

app = typer.Typer()


# change sound
@app.command("volume", help="Change system sound volume")
def change_sound(value: int = typer.Argument(..., help="Volume level (0-100)")):
    mac_settings.adjust_sound(value)


# mute sound
@app.command("mute", help="Mute system sound")
def mute_sound():
    mac_settings.mute_sound()


# unmute sound
@app.command("unmute", help="Unmute system sound")
def unmute_sound():
    mac_settings.unmute()


# clear system menu
@app.command("clear", help="Clear the recent system menu entries")
def clear_menu(target: str = typer.Argument(..., help="pass target: menu")):
    if target:
        mac_settings.recent_clear_menu()


@app.command("sleep", help="Put the system to sleep")
def sleep_mode():
    mac_settings.sleep_mode()
