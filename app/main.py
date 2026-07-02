from ast import arguments
import typer

app = typer.Typer()


@app.command()
def greet(
    name: str = typer.Argument(help="this shows you name"),
    age: int = typer.Option(min=10, help="this shows your age"),
):
    print(f"{name} and the age is {age}")


app()
