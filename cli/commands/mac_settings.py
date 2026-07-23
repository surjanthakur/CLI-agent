import typer
from rich import print

from ..tools.macos import mac_settings

app = typer.Typer()


# change sound
@app.command("sound", help="Change system sound volume")
def change_sound(value: int = typer.Argument(..., help="Volume level (0-100)")):
    try:
        mac_settings.adjust_sound(value)

    except Exception:
        pass
    else:
        print(f"[green] set volume level to {value}[/green]")


# mute sound
@app.command("mute", help="Mute system sound")
def mute_sound():
    try:
        mac_settings.mute_sound()

    except Exception:
        pass
    else:
        print("[green]set volume level to mute[/green]")


# unmute sound
@app.command("unmute", help="Unmute system sound")
def unmute_sound():
    try:
        mac_settings.unmute()

    except Exception:
        pass
    else:
        print("[green]set previous mute level to unmute[/green]")


# clear system menu
@app.command("clear", help="Clear the recent system menu entries")
def clear_menu(target: str = typer.Argument(..., help="pass target: menu")):
    try:
        if target:
            mac_settings.recent_clear_menu()

    except Exception:
        pass
    else:
        print("[green]Cleared Recent Menu[/green]")


# put mac on sleep mode
@app.command("sleep", help="Put the system to sleep")
def sleep_mode():
    try:
        mac_settings.sleep_mode()

    except Exception:
        pass
    else:
        print("[green]put mac on sleep mode[/green]")


# lock the screen
@app.command("lock", help="lock the system")
def lock_mode():
    try:
        mac_settings.lock_screen()
    except Exception:
        pass
    else:
        print("[green]locked your mac[/green]")
