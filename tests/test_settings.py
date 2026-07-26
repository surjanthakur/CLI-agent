import pytest
from typer.testing import CliRunner

from src.clark.commands import mac_settings

runner = CliRunner()


@pytest.mark.parametrize(
    ("command_name", "args", "method_name", "expected_output"),
    [
        ("sound", ["40"], "adjust_sound", "set volume level"),
        ("mute", [], "mute_sound", "set volume level to mute"),
        ("unmute", [], "unmute", "set previous mute level to unmute"),
        ("clear", ["menu"], "recent_clear_menu", "Cleared Recent Menu"),
        ("sleep", [], "sleep_mode", "put mac on sleep mode"),
        ("lock", [], "lock_screen", "locked your mac"),
    ],
)
# test all mac settings commands
def test_settings_commands_call_expected_helper(
    monkeypatch, command_name, args, method_name, expected_output
):
    called = {}

    def fake_handler(*value):
        called["value"] = value

    monkeypatch.setattr(mac_settings.mac_settings, method_name, fake_handler)

    result = runner.invoke(mac_settings.app, [command_name, *args])

    assert result.exit_code == 0
    assert expected_output in result.stdout
