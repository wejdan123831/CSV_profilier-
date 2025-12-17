# main 

import json
import csv
import profiling
import render 
from pathlib import Path
import io_handler
#
CSV_PATH = Path(r"C:\Users\w\Documents\my_csv_project\csv-profiler\src\saudi_shopping_with_missing2.csv")
def generate_profile():
    
    if not CSV_PATH.exists():
        print(f"Error: File not found at {CSV_PATH}")
        return
    
    

    data, headers = io_handler.read_csv(CSV_PATH) 
    if not headers:
        print("The CSV file is empty or has no headers.")
        return
    report = {
        "rows": 0,
        "columns": {}
    }
        # the columns
    for h in headers:
            report["columns"][h] = {"missing": 0, "type": "number", "_temp_types": set()} # dict for evry column 

    for row in data:
        report["rows"] += 1
        for h in headers:
            val = row[h]
            if profiling.is_missing(val):
                report["columns"][h]["missing"] += 1
            else:
                # 
                if not report["columns"][h]["_temp_types"]:
                    dtype = profiling.get_data_type(val)
                    report["columns"][h]["_temp_types"].add(dtype)
    # each colume data type
     
    for h in headers:
        types = report["columns"][h].pop("_temp_types")
        if "string" in types:
            report["columns"][h]["type"] = "string"
        elif "number" in types:
            report["columns"][h]["type"] = "number"
        else:
            report["columns"][h]["type"] = "unknown"

    # 1.  save report.json
    base_output = CSV_PATH.parent / "data_profile_report"
    
    render.generate_json(report, base_output)
    render.generate_md(report, base_output)
    
    #render.generate_json(report ,CSV_PATH)
    #render.generate_md(report , CSV_PATH)
   
    print("Done! report.json and report.md have been created successfully.")

  ## run only if the main   

if __name__ == "__main__":
    generate_profile()
  
  