
 # cli.py
import typer
from pathlib import Path
from typing_extensions import Annotated 


from . import io_handler  
from . import profiling   
from . import render


app = typer.Typer()

@app.command()
def main(
    path: Annotated[Path, typer.Argument(help="Path to the CSV file to profile")]
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

       
        base_output = path.parent / "data_profile_report"
        render.generate_json(report, base_output)
        render.generate_md(report, base_output)
        
        typer.secho(f" Done! Reports created at: {path.parent}", fg=typer.colors.GREEN, bold=True)

    except Exception as e:
        typer.secho(f" An error occurred: {e}", fg=typer.colors.RED)

# 6. 
if __name__ == "__main__":
    app()