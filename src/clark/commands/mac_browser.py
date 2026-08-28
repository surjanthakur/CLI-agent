import typer
from rich import print
from ytmusicapi import YTMusic

from ..core.logging import my_logger
from ..tools.macos import browser

app = typer.Typer()
yt = YTMusic()


# browser search
@app.command("search")
def search_command(
    query: str = typer.Option(..., "--q", help="Search query"),
):
    """this command search query in browser"""
    try:
        if not query:
            print("[red] enter your query to search e.g. --q 'who i am' ")
            raise typer.Exit()

        browser.search_browser(query=query.title())
        my_logger.info("call the search_browser function")

    except KeyboardInterrupt:
        my_logger.warning("KeyboardInterrupt during search_command")
        print("[red]you quit the M-copilot [/red]")
    else:
        print(f"[green]searching for... {query.title()}\n")


# play song
@app.command("play")
def play_song(song: list[str] = typer.Argument(..., help="song name")):  # noqa: B008
    """this function play song in ytmusic on your default set browser"""
    try:
        concate_song = " ".join(song).title()

        search_song = yt.search(query=concate_song, filter="songs")
        my_logger.info(f"search for the song {concate_song}")

        if not search_song:
            print("[red]Can't find song. Check spelling again.[/red]\n")
            raise typer.Exit(1)

        song_id = search_song[0].get("videoId")

        if not song_id:
            my_logger.error("song ID not found")
            print("[red]song ID not found.[/red]")
            raise typer.Exit()

        my_logger.info(f"get the song ID {song_id}")

        typer.launch(
            url=f"https://music.youtube.com/watch?v={song_id}",
            wait=True,
            locate=True,
        )
        my_logger.info("launch the typer_launch function")

    except KeyboardInterrupt:
        my_logger.warning("KeyboardInterrupt during play_song")
        print("[red]user quit the play command [/red]")

    except RuntimeError:
        my_logger.error("can't find song for the query")
    else:
        print(f"[green]playing song... {concate_song} on ytMusic.\n")
