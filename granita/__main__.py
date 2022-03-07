import typer
import pathlib

app = typer.Typer()


@app.callback()
def callback():
    """Welcome to Granita, a simple static site generator!

    If you're feeling kind you can buy me a coffee here 🍏 https://www.buymeacoffee.com/applephi"""


@app.command()
def init(name: str):
    """Initialize a new Granita project."""
    root = pathlib.Path(name)
    (root / "templates").mkdir(parents=True)
    (root / "static").mkdir(parents=True)
    (root / "pages").mkdir(parents=True)
    (root / "templates" / "default.html").write_text(
        """<html>
	<head>
		<link
			rel="stylesheet"
			href="https://unpkg.com/@picocss/pico@latest/css/pico.min.css"
		/>
	</head>
	<body>
		<div
			style="
				width: 60%;
				height: 50%;
				position: absolute;
				top: 0;
				bottom: 0;
				left: 0;
				right: 0;
				margin: auto;
			"
		>
			<content />
		</div>
	</body>
</html>
"""
    )
    (root / "pages" / "index.md").write_text(
        """---
title: "Granita"
---
# Hello world
Welcome to your first Granita project!

> *If you're feeling kind you can buy me a coffee [here](https://www.buymeacoffee.com/applephi)* 🍏"""
    )


@app.command()
def build(
    clean: bool = typer.Argument(
        False, help="Whether to clean out the public folder before building."
    )
):
    """Render templates to HTML."""
    from .transform import build

    build(clean)


if __name__ == "__main__":
    app(prog_name="granita")
