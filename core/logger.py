from rich.console import Console

console = Console(style="white")

def log_info(msg: str):
    console.print(f"[bold white][INFO][/bold white] {msg}")

def log_success(msg: str):
    console.print(f"[bold white][SUCCESS][/bold white] {msg}")

def log_error(msg: str):
    console.print(f"[bold white][ERROR][/bold white] {msg}")

def log_warning(msg: str):
    console.print(f"[bold white][WARNING][/bold white] {msg}")
