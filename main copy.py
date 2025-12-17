import csv
import json


CSV_PATH = r"C:\Users\w\Documents\AI camp\saudi_shopping_with_missing.csv"

def generate_profile():
    
    report = {
        "rows": 0,
        "columns": {}
    }


    with open(CSV_PATH, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file) # read evry row and convert it into dict { the columns name it is the key and the value it is the cell content }
        headers = reader.fieldnames  # get all columns name and store it in headers list 

        # the columns
        for h in headers:
            report["columns"][h] = {"missing": 0, "type": "number", "_temp_types": set()} # dict for evry column 

        # get all the data 
        for row in reader:
            report["rows"] += 1
            for h in headers:
                val = row[h].strip()
                if val == "":
                    report["columns"][h]["missing"] += 1
                else:
                    try:
                        float(val)
                        report["columns"][h]["_temp_types"].add("number")
                    except ValueError:
                        report["columns"][h]["_temp_types"].add("string")

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
    with open("report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)

    # 2.  save report.md   
    with open("report.md", "w", encoding="utf-8") as f:
        f.write("# Project Data Profile Report\n\n")
        f.write(f"**Total Rows:** {report['rows']}\n\n")
        f.write("| Column Name | Missing Values | Data Type |\n")
        f.write("| :--- | :--- | :--- |\n")
        for col, info in report["columns"].items():
            f.write(f"| {col} | {info['missing']} | {info['type']} |\n")

    print("Done! report.json and report.md have been created successfully.")

    
       

if __name__ == "__main__":
    generate_profile()
    
   
   
   
    # this is the secound copy of my work 
 # import csv
import json


CSV_PATH = r"C:\Users\w\Documents\AI camp\saudi_shopping_with_missing.csv"

def get_data_type(value):
    val = value.strip()
    if not val: return None
    try:
        float(val)
        return "number"
    except ValueError:
        return "string"
   
def is_missing(value: str | None) -> bool:
    if value is None:
        return True
    
    val = value.strip().lower()
    
    blacklist = [
        "",       
        "na",    
        "n/a",    
        "null",   
        "none",   
        "nan"     
    ]
    
    return val in blacklist

def generate_profile():
    
    report = {
        "rows": 0,
        "columns": {}
    }


    with open(CSV_PATH, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file) # read evry row and convert it into dict { the columns name it is the key and the value it is the cell content }
        headers = reader.fieldnames  # get all columns name and store it in headers list 

        # the columns
        for h in headers:
            report["columns"][h] = {"missing": 0, "type": "number", "_temp_types": set()} # dict for evry column 

       
       # get all the data 
        for row in reader:
            report["rows"] +=1
            for h in headers:  
                val = row[h]
                
                if is_missing(val):
                    report["columns"][h]["missing"] += 1
                else: 
                    if not report["columns"][h]["_temp_types"]: # ckek it is not the first value 
                     dtype = get_data_type(val)
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
    with open("report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)

    # 2.  save report.md   
    with open("report.md", "w", encoding="utf-8") as f:
        f.write("# Project Data Profile Report\n\n")
        f.write(f"**Total Rows:** {report['rows']}\n\n")
        f.write("| Column Name | Missing Values | Data Type |\n")
        f.write("| :--- | :--- | :--- |\n")
        for col, info in report["columns"].items():
            f.write(f"| {col} | {info['missing']} | {info['type']} |\n")

    print("Done! report.json and report.md have been created successfully.")

  ## run only if the main   

if __name__ == "__main__":
    generate_profile()
 
 # this is the third copy of my work in the main we have read csv file and generate disc 
 
 
import json
import csv
import profiling
import render 
CSV_PATH = r"C:\Users\w\Documents\AI camp\saudi_shopping_with_missing.csv"


def generate_profile():
    
    report = {
        "rows": 0,
        "columns": {}
    }

    
    with open(CSV_PATH, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file) # read evry row and convert it into dict { the columns name it is the key and the value it is the cell content }
        headers = reader.fieldnames  # get all columns name and store it in headers list 

        # the columns
        for h in headers:
            report["columns"][h] = {"missing": 0, "type": "number", "_temp_types": set()} # dict for evry column 

       
       # get all the data 
        for row in reader:
            report["rows"] +=1
            for h in headers:  
                val = row[h]
                
                if profiling.is_missing(val):
                    report["columns"][h]["missing"] += 1
                else: 
                    if not report["columns"][h]["_temp_types"]: # ckek it is not the first value 
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
    render.generate_json(report ,CSV_PATH)
    render.generate_md(report , CSV_PATH)
  
    print("Done! report.json and report.md have been created successfully.")

  ## run only if the main   

if __name__ == "__main__":
    generate_profile()
 
 