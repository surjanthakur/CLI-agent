import sentry_sdk
import typer

from .commands import mac_apps, mac_browser, mac_settings
from .core.logging import init_sentry_logs, my_logger

app = typer.Typer(help="""
    [green]clark cli lets you control macOS apps, browser actions, and system settings from the terminal.
    Made With ❤️ by Surjan thakur""")


# mac app commands
app.command(name="open", help="[red] Open an application or file.")(
    mac_apps.open_command
)

app.command(name="close", help="[red] Close an application.")(mac_apps.close_command)

app.command(name="hide", help="[red] Hide the current application.")(
    mac_apps.hide_command
)

app.command(name="unhide", help="[red] Unhide a previously hidden application.")(
    mac_apps.unhide_command
)

# system setting commands
app.command(name="sound", help="[yellow]Adjust the system volume.")(
    mac_settings.change_sound
)

app.command(name="mute", help="[yellow]Mute system audio.")(mac_settings.mute_sound)

app.command(name="unmute", help="[yellow]Unmute system audio.")(
    mac_settings.unmute_sound
)

app.command(name="clear", help="[yellow]Clear the current menu or terminal state.")(
    mac_settings.clear_menu
)

app.command(name="sleep", help="[yellow]Put the ststem to sleep.")(
    mac_settings.sleep_mode
)

app.command(name="lock", help="[yellow]Lock the system screen.")(mac_settings.lock_mode)

# browser commands
app.command(name="search", help="[bold blue]Search a query in the browser.")(
    mac_browser.search_command
)

app.command(name="play", help="[bold blue]Play a song in browser-based music.")(
    mac_browser.play_song
)


# run neo cli app
def clark_cli_app():
    my_logger.info("Application starting")
    try:
        my_logger.info("Starting CLI app")
        init_sentry_logs()
        app()

    except KeyboardInterrupt:
        my_logger.warning("Application interrupted by user ")
        raise
    except Exception:
        my_logger.exception("Application failed")
        raise
    finally:
        my_logger.info("Application stopped")
        sentry_sdk.flush(timeout=0.2)


if __name__ == "__main__":
    clark_cli_app()
