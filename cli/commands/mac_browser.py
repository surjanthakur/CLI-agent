from typing import List

import typer
from rich import print
from ytmusicapi import YTMusic

from ..core.logging import logger
from ..tools.macos import browser

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
            print("[red]Can't find song. Check spelling again.[/red]\n")
            raise typer.Exit(1)

        song_id = search_song[0].get("videoId")

        if not song_id:
            print("[red]Video ID not found.[/red]")
            raise typer.Exit()

        typer.launch(
            url=f"https://music.youtube.com/watch?v={song_id}",
            wait=True,
            locate=True,
        )
    except RuntimeError:
        logger.error("can't find song for the query")
    else:
        print(f"[green]playing song... {concate_song} on ytMusic.\n")
