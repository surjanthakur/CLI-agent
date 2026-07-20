from .mac_apps import open_command, close_command, hide_command, unhide_command
from .mac_settings import change_sound, mute_sound, unmute_sound
import typer

app = typer.Typer()


# mac apps commands
app.command(name="open")(open_command)
app.command(name="close")(close_command)
app.command(name="hide")(hide_command)
app.command(name="unhide")(unhide_command)

app.command(name="volume")(change_sound)
app.command(name="mute")(mute_sound)
app.command(name="unmute")(unmute_sound)
