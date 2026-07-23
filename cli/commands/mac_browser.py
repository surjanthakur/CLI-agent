from ..core.logging import logger
from ..tools.macos import browser

from rich import print
from typing import List
from ytmusicapi import YTMusic
import typer

app = typer.Typer()

yt = YTMusic()


# browser search
@app.command("search")
def search_command(
    query: str = typer.Option(..., "--q", help="Search query"),
):
    """this command search query in safari browser"""
    try:

        if not query:
            print("[red] enter your query to search e.g. --q 'who i am' ")
            raise typer.Exit()
        browser.search_browser(query=query.title())

    except Exception:
        pass
    else:
        print(f"[green]searching for... {query.title()}\n")


# play song
@app.command("play")
def play_song(song: List[str] = typer.Argument(..., help="song name")):
    try:
        concate_song = " ".join(song).title()

        search_song = yt.search(query=concate_song, filter="songs")

        if not search_song:
            print("[red]Can't find song. Check spelling again.[/red]")
            raise typer.Exit()

        song_id = search_song[0].get("videoId")

        if not song_id:
            print("[red]Video ID not found.[/red]")
            raise typer.Exit()

        typer.launch(
            url=f"https://music.youtube.com/watch?v={song_id}",
            wait=True,
            locate=True,
        )

    except Exception as err:
        print("[red] someting went wrong try again [/red]")
        logger.exception(err)
