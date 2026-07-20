from .mac_apps import open_command, close_command, hide_command, unhide_command
from .mac_settings import (
    change_sound,
    mute_sound,
    unmute_sound,
    clear_menu,
    sleep_mode,
)

import typer

app = typer.Typer()


# mac apps commands
app.command(name="open")(open_command)
app.command(name="close")(close_command)
app.command(name="hide")(hide_command)
app.command(name="unhide")(unhide_command)

# system settings commands
app.command(name="volume")(change_sound)
app.command(name="mute")(mute_sound)
app.command(name="unmute")(unmute_sound)
app.command(name="clear")(clear_menu)
app.command(name="sleep")(sleep_mode)
