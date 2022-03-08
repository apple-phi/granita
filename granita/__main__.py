import typer
import shutil
import pathlib

app = typer.Typer()


@app.callback()
def callback():
    """Welcome to Granita, a simple static site generator!

    If you're feeling kind you can buy me a coffee here 🍏 https://www.buymeacoffee.com/applephi"""


@app.command()
def init(name: str):
    """Initialize a new Granita project."""
    shutil.copytree(pathlib.Path(__file__).parent / "init", name)


@app.command()
def build(
    clean: bool = typer.Option(
        False, help="Whether to clean out the public folder before building."
    )
):
    """Render templates to HTML."""
    from .transform import build

    build(clean)


if __name__ == "__main__":
    app(prog_name="granita")
