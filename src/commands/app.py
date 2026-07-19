from .mac_apps import open_command, close_command, hide_command, unhide_command
from .chat import chat_command

import typer

app = typer.Typer()

app.command(name="open")(open_command)
app.command(name="close")(close_command)
app.command(name="hide")(hide_command)
app.command(name="unhide")(unhide_command)
app.command(name="chat")(chat_command)
