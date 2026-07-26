import pytest
from typer.testing import CliRunner

from src.clark.commands import mac_apps

runner = CliRunner()


@pytest.mark.parametrize(
    ("command_name", "method_name"),
    [
        ("open", "open_app"),
        ("close", "close_app"),
        ("hide", "hide_app"),
        ("unhide", "unhide_app"),
    ],
)
def test_app_commands_call_expected_helper(monkeypatch, command_name, method_name):
    called = {}

    def fake_handler(name: str):
        called["name"] = name

    monkeypatch.setattr(mac_apps.apps, method_name, fake_handler)

    result = runner.invoke(mac_apps.app, [command_name, "Notes"])

    assert result.exit_code == 0
    assert called["name"] == "Notes"
