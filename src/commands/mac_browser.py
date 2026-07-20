import typer
from ..tools.macos import browser

app = typer.Typer()


@app.command("search")
def search_command(
    query: str = typer.Option(..., "--q", help="Search query"),
):
    if not query:
        typer.echo("Error: Provide search terms with --q")
        raise typer.Exit()

    query_formatted = query.title()

    browser.search_browser(query_formatted)
