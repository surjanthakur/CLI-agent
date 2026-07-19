from common import subprocess


# open mac app func
def open_app(app_name: str):
    """this function open the mac apps"""
    script = f'tell application "{app_name}" to activate'
    subprocess.run_process(script)


# close mac app func
def close_app(app_name: str):
    """this function close the mac apps"""
    script = f'tell application "{app_name}" to activate'
    subprocess.run_process(script)


def hide_app(app_name: str):
    """this function hide the mac apps"""
    script = f"tell application {app_name} hide end tell"
    subprocess.run_process(script)


def unhide_app(app_name: str):
    script = f'tell application "{app_name}" to activate'
    subprocess.run_process(script)
