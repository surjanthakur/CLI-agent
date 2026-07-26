import sentry_sdk
import typer

from .commands.mac_apps import close_command, hide_command, open_command, unhide_command
from .commands.mac_browser import play_song, search_command
from .commands.mac_settings import (
    change_sound,
    clear_menu,
    lock_mode,
    mute_sound,
    sleep_mode,
    unmute_sound,
)
from .core.logging import my_logger

app = typer.Typer(help="""
    [green]clark cli lets you control macOS apps, browser actions, and system settings from the terminal.
    Made With ❤️ by Surjan Thakur""")


# mac app commands
app.command(name="open", help="[red] Open an application or file.")(open_command)

app.command(name="close", help="[red] Close an application.")(close_command)

app.command(name="hide", help="[red] Hide the current application.")(hide_command)

app.command(name="unhide", help="[red] Unhide a previously hidden application.")(
    unhide_command
)

# system setting commands
app.command(name="sound", help="[yellow]Adjust the system volume.")(change_sound)

app.command(name="mute", help="[yellow]Mute system audio.")(mute_sound)

app.command(name="unmute", help="[yellow]Unmute system audio.")(unmute_sound)

app.command(name="clear", help="[yellow]Clear the current menu or terminal state.")(
    clear_menu
)

app.command(name="sleep", help="[yellow]Put the ststem to sleep.")(sleep_mode)

app.command(name="lock", help="[yellow]Lock the system screen.")(lock_mode)

# browser commands
app.command(name="search", help="[bold blue]Search a query in the browser.")(
    search_command
)

app.command(name="play", help="[bold blue]Play a song in browser-based music.")(
    play_song
)


# run neo cli app
def neo_cli_app():
    my_logger.info("Application starting")
    try:
        my_logger.info("Starting CLI app")
        app()

    except KeyboardInterrupt:
        my_logger.warning("Application interrupted by user")
        raise

    except Exception:
        my_logger.exception("Application failed")
        raise
    finally:
        my_logger.info("Application stopped")
        sentry_sdk.flush(timeout=0.2)


if __name__ == "__main__":
    neo_cli_app()
