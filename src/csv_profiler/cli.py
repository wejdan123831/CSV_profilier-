import typer
from pathlib import Path
from typing import Optional 
from typing_extensions import Annotated 

from . import io_handler  
from . import profiling    
from . import render

app = typer.Typer()

@app.command()
def main(
    path: Annotated[Path, typer.Argument(help="Path to the CSV file to profile")],
    out_dir: Annotated[str, typer.Option(help="Output directory")] = "outputs",
    format: Annotated[str, typer.Option(help="Output format (json, md, both)")] = "both"
):
    if not path.exists():
        typer.secho(f" Error: File not found at {path}", fg=typer.colors.RED, bold=True)
        raise typer.Exit(code=1)

    typer.echo(f" Reading and analyzing: {path.name}...")

    try:
        data, headers = io_handler.read_csv(path) 
        
        if not headers:
            typer.echo(" The CSV file is empty or has no headers.")
            return

        report = profiling.profile_csv(data, headers)

       
        output_path = Path(out_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        base_output = output_path / path.stem

       
        if format in ["json", "both"]:
            render.generate_json(report, base_output)
            typer.echo(f" JSON report saved.")
            
        if format in ["md", "both"]:
            render.generate_md(report, base_output)
            typer.echo(f" Markdown report saved.")
        
        typer.secho(f" Done! Reports created in: {out_dir}", fg=typer.colors.GREEN, bold=True)

    except Exception as e:
        typer.secho(f" An error occurred: {e}", fg=typer.colors.RED)

if __name__ == "__main__":
    app()