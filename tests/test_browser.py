from typer.testing import CliRunner

from src.clark.commands import mac_browser

runner = CliRunner()


def test_search_command_calls_browser(monkeypatch):
    called = {}

    def fake_search(query: str):
        called["query"] = query

    monkeypatch.setattr(mac_browser.browser, "search_browser", fake_search)

    result = runner.invoke(mac_browser.app, ["search", "--q", "hello world"])

    assert result.exit_code == 0
    assert called["query"] == "Hello World"
    assert "searching for" in result.stdout


def test_play_song_command_launches_youtube_url(monkeypatch):
    launched = {}

    class FakeYTMusic:
        def search(self, query: str, filter: str):
            assert query == "Song Name"
            assert filter == "songs"
            return [{"videoId": "abc123"}]

    monkeypatch.setattr(mac_browser, "yt", FakeYTMusic())
    monkeypatch.setattr(
        mac_browser.typer,
        "launch",
        lambda **kwargs: launched.update(kwargs),
    )

    result = runner.invoke(mac_browser.app, ["play", "song", "name"])

    assert result.exit_code == 0
    assert launched["url"] == "https://music.youtube.com/watch?v=abc123"
    assert "playing song" in result.stdout
