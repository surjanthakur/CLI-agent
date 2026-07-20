from .mac_apps import open_command, close_command, hide_command, unhide_command
from .mac_settings import app as setting_app

import typer

app = typer.Typer()
app.add_typer(
    setting_app,
    name="sound",
    help="commands helps user to control mac settings",
)

# mac apps commands
app.command(name="open")(open_command)
app.command(name="close")(close_command)
app.command(name="hide")(hide_command)
app.command(name="unhide")(unhide_command)
