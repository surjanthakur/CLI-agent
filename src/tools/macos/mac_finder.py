from ..common import subprocess


# open mac app
def open_app(app_name: str):
    """this function open the mac apps"""
    script = f'tell application "{app_name.title()}" to activate'
    subprocess.run_process(script)


# close mac app
def close_app(app_name: str):
    """this function close the mac apps"""
    script = f'tell application "{app_name.title()}" to quit'
    subprocess.run_process(script)


# hide mac app
def hide_app(app_name: str):
    """this function hide the mac apps"""
    script = f"tell application {app_name.title()} hide end tell"
    subprocess.run_process(script)


# unhide mac app
def unhide_app(app_name: str):
    """this function unhide the mac apps"""
    script = f'tell application "{app_name.title()}" to activate'
    subprocess.run_process(script)
