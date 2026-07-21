import typer
from ..tools.macos import browser
from ..utils.exceptions import handle_exceptions

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
    handle_exceptions(browser.search_browser, query_formatted)
