from ..common import run_script
import typer


def search_browser(query: str):
    """this function Search in specified browser"""
    script = f"""
         tell application "Safari"
            activate
            
            if not (exists window 1) then
                make new document
            else
                tell window 1 to make new tab at end of tabs
            end if
            
            delay 0.4
            
            tell window 1's current tab
                set URL to "https://www.google.com/search?q=" & quoted form of "{query}"
            end tell
        end tell
      """
    try:
        run_script.run_process(script)

    except RuntimeError as err:
        typer.secho(
            "oops! can't open browser, try again ❌",
            fg=typer.colors.RED,
        )
