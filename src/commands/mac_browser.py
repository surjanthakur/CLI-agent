import typer
from ..tools.macos import browser

app = typer.Typer()


# browser search
@app.command("search")
def search_command(
    query: str = typer.Option(..., "--q", help="Search query"),
):
    """this command search query in safari browser"""

    if not query:
        typer.echo("Error: Provide search terms with --q")
        raise typer.Exit()

    query_formatted = query.title()

    browser.search_browser(query_formatted)
