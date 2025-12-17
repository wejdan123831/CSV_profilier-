# render.py
import json
from pathlib import Path
from typing import Dict, Any

def generate_json(report: Dict[str, Any], output_path: Path) -> None:
    
   
    final_path = output_path.with_suffix('.json') if output_path.suffix != '.json' else output_path
    with open(final_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)
    print(f" JSON report saved to: {final_path}")

def generate_md(report: Dict[str, Any], output_path: Path) -> None:
    
    if not report.get("rows"):
        print("the report is empty .")
        return

    final_path = output_path.with_suffix('.md') if output_path.suffix != '.md' else output_path
    with open(final_path, "w", encoding="utf-8") as f:
        f.write("# Project Data Profile Report\n\n")
        f.write(f"**Total Rows:** {report['rows']}\n\n")
        f.write("| Column Name | Missing Values | Data Type |\n")
        f.write("| :--- | :--- | :--- |\n")
        
        for col, info in report["columns"].items():
            f.write(f"| {col} | {info['missing']} | {info['type']} |\n")
    print(f" Markdown report saved to: {final_path}")