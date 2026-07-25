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

app = typer.Typer(
    help="mac-cli-agent lets you control macOS apps, browser actions, and system settings from the terminal."
)


# mac app commands
app.command(name="open", help="Open an application or file.")(open_command)

app.command(name="close", help="Close an application.")(close_command)

app.command(name="hide", help="Hide the current application.")(hide_command)

app.command(name="unhide", help="Unhide a previously hidden application.")(
    unhide_command
)

# system setting commands
app.command(name="sound", help="Adjust the system volume.")(change_sound)

app.command(name="mute", help="Mute system audio.")(mute_sound)

app.command(name="unmute", help="Unmute system audio.")(unmute_sound)

app.command(name="clear", help="Clear the current menu or terminal state.")(clear_menu)

app.command(name="sleep", help="Put the computer to sleep.")(sleep_mode)

app.command(name="lock", help="Lock the computer screen.")(lock_mode)

# browser commands
app.command(name="search", help="Search a query in the browser.")(search_command)

app.command(name="play", help="Play a song in browser-based music.")(play_song)


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


if __name__ == "__main__":
    neo_cli_app()
