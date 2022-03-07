import typer

from .transform import build


app = typer.Typer()


@app.command()
def main(
    clean: bool = typer.Argument(
        False, help="Whether to clean out the public folder before building."
    )
):
    """Welcome to Granita, a simple static site generator!

    If you're feeling kind you can buy me a coffee here 🍏 https://www.buymeacoffee.com/applephi"""
    build(clean)


if __name__ == "__main__":
    app(prog_name="granita")
