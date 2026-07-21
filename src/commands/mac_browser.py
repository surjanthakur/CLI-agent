import typer
from ..tools.macos import browser
from ..core.logging import logger
from ..utils.exceptions import SubprocessRunningError
from rich import print

app = typer.Typer()


# browser search
@app.command("search")
def search_command(
    query: str = typer.Option(..., "--q", help="Search query"),
):
    """this command search query in safari browser"""
    try:
        if not query:
            typer.echo("Error: Provide search terms with --q")
            raise typer.Exit()

        query_formatted = query.title()
        browser.search_browser(query_formatted)

    except SubprocessRunningError as err:
        logger.error(
            f"subprocess error:{err.message}",
            extra={
                "returncode": err.returncode,
                "stdout": err.stdout,
                "stderr": err.stderr,
            },
        )
        print("[bold blue]something went wrong to search query[/bold blue]try again!")
        typer.Exit()
