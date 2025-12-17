# profiling.py
from typing import List, Dict, Any

def get_data_type(value: str) -> str:
    val = value.strip()
    if not val: return None
    try:
        float(val)
        return "number"
    except ValueError:
        return "string"

def is_missing(value: str | None) -> bool:
    if value is None: return True
    val = value.strip().lower()
    blacklist = ["", "na", "n/a", "null", "none", "nan"]
    return val in blacklist

def profile_csv(data: List[Dict], headers: List[str]) -> Dict[str, Any]:
   
    report = {
        "rows": 0,
        "columns": {}
    }

    # 
    for h in headers:
        report["columns"][h] = {"missing": 0, "type": "number", "_temp_types": set()}

    # 
    for row in data:
        report["rows"] += 1
        for h in headers:
            val = row.get(h, "")
            if is_missing(val):
                report["columns"][h]["missing"] += 1
            else:
                if not report["columns"][h]["_temp_types"]:
                    dtype = get_data_type(val)
                    report["columns"][h]["_temp_types"].add(dtype)

    # 
    for h in headers:
        types = report["columns"][h].pop("_temp_types")
        if "string" in types:
            report["columns"][h]["type"] = "string"
        elif "number" in types:
            report["columns"][h]["type"] = "number"
        else:
            report["columns"][h]["type"] = "unknown"
            
    return report