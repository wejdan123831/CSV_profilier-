import json
from pathlib import Path
from typing import Dict, Any

def generate_json(report: Dict[str, Any], output_path: Path = None) -> str:
    json_content = json.dumps(report, indent=4, ensure_ascii=False)
    
    
    if output_path:
        final_path = output_path.with_suffix('.json')
        with open(final_path, "w", encoding="utf-8") as f:
            f.write(json_content)
        print(f"✅ JSON report saved to: {final_path}")
    
    return json_content

def generate_md(report: Dict[str, Any], output_path: Path = None) -> str:
    if not report.get("rows"):
        return "The report is empty."

  
    md_content = "# 📊 Project Data Profile Report\n\n"
    md_content += f"**Total Rows:** {report['rows']}\n\n"
    md_content += "| Column Name | Missing Values | Data Type |\n"
    md_content += "| :--- | :--- | :--- |\n"
    
    
    columns = report.get("columns", {})
    for col, info in columns.items():
      
        missing = info.get('missing', 'N/A')
        dtype = info.get('type', 'N/A')
        md_content += f"| {col} | {missing} | {dtype} |\n"

   
    if output_path:
        final_path = output_path.with_suffix('.md')
        with open(final_path, "w", encoding="utf-8") as f:
            f.write(md_content)
        print(f"✅ Markdown report saved to: {final_path}")
    
    return md_content