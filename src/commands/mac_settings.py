from tools.macos import mac_settings

import typer

app = typer.Typer()


@app.command("volume", help="Change system sound volume")
def change_sound(value: int = typer.Argument(..., help="Volume level (0-100)")):
    mac_settings.adjust_sound(value)


@app.command("mute", help="Mute system sound")
def mute_sound():
    mac_settings.mute_sound()


@app.command("unmute", help="Unmute system sound")
def unmute_sound():
    mac_settings.unmute()


@app.command("brightness", help="set system brightness")
def set_brightness(value: int = typer.Argument(..., help="brightness level (0-100)")):
    mac_settings.set_brightness(value)
