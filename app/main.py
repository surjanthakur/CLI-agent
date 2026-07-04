import typer
from requests import request

app = typer.Typer(name="nova")


@app.command("weather")
def check_weather(city: str = typer.Option(...)):
    req = request(
        method="GET",
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=04686a7ac53877a0115b545489c9fac1&units=metric",
    )
    if req.status_code == 200:
        data = req.json()


app()
