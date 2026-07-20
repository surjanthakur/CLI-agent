from .mac_apps import open_command, close_command, hide_command, unhide_command
from .mac_settings import app as settings_app

import typer

app = typer.Typer()
app.add_typer(
    settings_app,
    name="set",
    help="control the mac settings e.g. sound , brigtness.",
)

# mac apps commands
app.command(name="open")(open_command)
app.command(name="close")(close_command)
app.command(name="hide")(hide_command)
app.command(name="unhide")(unhide_command)
