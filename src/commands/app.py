from .mac_apps import open_command, close_command, hide_command, unhide_command
from .mac_settings import (
    change_sound,
    mute_sound,
    unmute_sound,
    clear_menu,
    sleep_mode,
    lock_mode,
)

import typer

app = typer.Typer()


# mac apps commands
app.command(
    name="open",
    help="Open an application or file",
)(open_command)
app.command(
    name="close",
    help="Close an application",
)(close_command)
app.command(
    name="hide",
    help="Hide the current application",
)(hide_command)
app.command(
    name="unhide",
    help="Unhide a previously hidden application",
)(unhide_command)

# system settings commands
app.command(name="sound", help="Adjust the system volume")(change_sound)
app.command(name="mute", help="Mute system audio")(mute_sound)
app.command(name="unmute", help="Unmute system audio")(unmute_sound)
app.command(name="clear", help="Clear the current menu or terminal state")(clear_menu)
app.command(name="sleep", help="Put the computer to sleep")(sleep_mode)
app.command(name="lock", help="Lock the computer screen")(lock_mode)
