class SubprocessRunningError(Exception):
    """Raised when an osascript subprocess fails."""

    def ___init__(
        self,
        message: str,
        *,
        returncode: int | None = None,
        stdout: str = "",
        stderr: str = "",
    ):
        self.message = message
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr
