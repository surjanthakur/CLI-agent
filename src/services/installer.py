import subprocess
from ..core.logging import logger

from rich.console import Console
from rich.progress import (
    Progress,
    SpinnerColumn,
    TextColumn,
    BarColumn,
    TimeElapsedColumn,
)
from rich import print as rprint

console = Console()


def download_ollama():
    """Install Ollama using Homebrew with a nice progress UI."""
    try:
        rprint("[bold blue]Installing Ollama via Homebrew...[/bold blue]")

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TimeElapsedColumn(),
            console=console,
            transient=False,  # Keep final status visible
        ) as progress:

            task = progress.add_task("Downloading & installing Ollama...", total=None)

            # Run brew install and stream output in real-time
            process = subprocess.Popen(
                ["brew", "install", "ollama"],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,  # Line buffered
            )

            # Stream brew's output while keeping the progress spinner alive
            if process.stdout:
                for line in process.stdout:
                    # Print brew's output (important for user to see what's happening)
                    console.print(line, end="")
                    # Optional: you can update description based on keywords if you want
                    if "Downloading" in line:
                        progress.update(task, description="Downloading Ollama...")
                    elif "Installing" in line or "Pouring" in line:
                        progress.update(task, description="Installing...")

            return_code = process.wait()

            if return_code == 0:
                progress.update(
                    task,
                    completed=100,
                    description="[green]Ollama installed successfully![/green]",
                )
                rprint("[bold green]✓ Ollama has been installed![/bold green]")
            else:
                progress.update(task, description="[red]Installation failed[/red]")
                rprint(
                    "[bold red]✗ Something went wrong during installation.[/bold red]"
                )
                raise subprocess.CalledProcessError(
                    return_code, ["brew", "install", "ollama"]
                )

    except FileNotFoundError:
        rprint(
            "[bold red]Error: 'brew' command not found. Is Homebrew installed?[/bold red]"
        )
    except subprocess.CalledProcessError as e:
        logger.error(f"Ollama installation failed: {e}")
        rprint("[red]Installation failed. Check the output above.[/red]")
    except Exception as e:
        logger.exception("Unexpected error")
        rprint(f"[red]Unexpected error: {e}[/red]")


def download_llm_model():
    """Install Ollama model qwen2.5-code:3b using Homebrew with a nice progress UI."""
    try:
        rprint(
            "[bold blue]Installing qwen2.5-coder:3b model via Homebrew...[/bold blue]"
        )
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TimeElapsedColumn(),
            console=console,
            transient=False,  # Keep final status visible
        ) as progress:
            task = progress.add_task(
                "Downloading & installing qwen2.5-coder...", total=None
            )
            process = subprocess.Popen(
                ["ollama", "pull", "qwen2.5-coder:3b"],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,  # Line buffered
            )

            # Stream brew's output while keeping the progress spinner alive
            if process.stdout:
                for line in process.stdout:
                    # Print brew's output (important for user to see what's happening)
                    console.print(line, end="")
                    # Optional: you can update description based on keywords if you want
                    if "Downloading" in line:
                        progress.update(
                            task, description="Downloading qwen2.5-coder:3b..."
                        )
                    elif "Installing" in line or "Pouring" in line:
                        progress.update(task, description="Installing...")

            return_code = process.wait()

            if return_code == 0:
                progress.update(
                    task,
                    completed=100,
                    description="[green]qwen2.5-coder:3b installed successfully![/green]",
                )
                rprint(
                    "[bold green]✓ qwen2.5-coder:3b has been installed![/bold green]"
                )
            else:
                progress.update(task, description="[red]Installation failed[/red]")
                rprint(
                    "[bold red]✗ Something went wrong during installation.[/bold red]"
                )
                raise subprocess.CalledProcessError(
                    return_code, ["brew", "install", "ollama"]
                )
    except FileNotFoundError:
        rprint(
            "[bold red]Error: 'brew' command not found. Is Homebrew installed?[/bold red]"
        )
    except subprocess.CalledProcessError as e:
        logger.error(f"qwen2.5-coder installation failed: {e}")
        rprint("[red]Installation failed. Check the output above.[/red]")
    except Exception as e:
        logger.exception("Unexpected error")
        rprint(f"[red]Unexpected error: {e}[/red]")
